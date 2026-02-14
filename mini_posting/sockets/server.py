import socket

HOST = "127.0.0.1"
PORT = 8080

def start_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET -> IPv4 adreslash, SOCK_STREAM - TCP protokoli
    server_socket.bind((HOST,PORT)) # server hostga bog'landi

    server_socket.listen(5)
    print(f"Server ishga tushdi: http://{HOST}:{PORT}")

    while True:
        client_socket, client_addr = server_socket.accept()
        print("Ulanish qabul qilindi:", client_addr)

        print(f"\nUlandi: {client_addr}")

        request = client_socket.recv(1024).decode("utf-8")
        print("-HTTP so'rov-")
        print(request)

        html_body = """
                <html>
                    <head>
                        <title>Mini HTTP Server</title>
                    </head>
                    <body>
                        <h1>Sarlavha</h1>
                        <p>Bu socket asosidagi HTTP server.</p>
                    </body>
                </html>
                """

        # HTTP javob (HTTP/1.1)
        response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                f"Content-Length: {len(html_body.encode('utf-8'))}\r\n"
                "Connection: close\r\n"
                "\r\n"
                + html_body
        )

        client_socket.sendall(response.encode("utf-8"))
        client_socket.close()