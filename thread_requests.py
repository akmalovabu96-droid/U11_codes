# 1.17 Python Threading, JSONplaceholder'ga parallel(concurrency) so'rovnoma yuborish
import threading
import time
import requests

# Har bir URL uchun funksiya
def send_request(url):
    try:
        response = requests.get(url)
        print(f"{url} -> Status: {response.status_code}")
    except Exception as e:
        print(f"{url} -> Xatolik: {e}")

# Asosiy qism
def main():
    baza = "https://jsonplaceholder.typicode.com"
    paths = ["/posts/1", "/posts/2", "/posts3/", "/posts/4", "/posts/5"] # Yo'llar

    # To'liq url ro'yxati
    urls = [baza + path for path in paths]
    # Thread'lar
    threads = [threading.Thread(target=send_request, args=(url,)) for url in urls]

    start = time.time()

    # Barcha thread'larni ishga tushirib, tugashini kutamiz
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    end = time.time()
    print(f"\nBarcha request'lar {end - start:.2f} soniyada tugadi.")

if __name__ == "__main__":
    main()


