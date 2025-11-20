# 1.15 normativ

import requests

bosh_url = "https://jsonplaceholder.typicode.com/"

# GET so'rovi
def get_post():
    print("GET so'rovi")
    response = requests.get(f"{bosh_url}/posts")
    print("Status code:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        print("Birinchi post:")
        print(data)

# POST so'rovi
def create_post():
    print("POST so'rovi")
    new_post = {
        "title": "Mening birinchi postim",
        "body": "Bu test post",
        "userId": 1
    }
    response = requests.post(f"{bosh_url}/posts", json=new_post)
    print("Status code", response.status_code)
    if response.status_code == 201:
        data = response.json()
        print("Yangi post:", data)
        print("Yangi post ID:", data.get("id"))

# PUT so'rovi
def update_post():
    print("PUT so'rovi")
    updated_post = {
        "title": "Yangilangan sarlavha",
        "body": "Yangilangan matn",
        "userId": 1
    }
    response = requests.put(f"{bosh_url}/posts/1", json=updated_post)
    print("Status code:", response.status_code)
    print("Yangilangan post:")
    print(response.json())

# DELETE so'rovi
def delete_post():
    print("DELETE so'rovi")
    response = requests.delete(f"{bosh_url}/post/1")
    print("Status code:", response.status_code)
    if response.status_code in [200, 204]:
        print("Muvaffaqiyatli o'chirildi")
    else:
        print("O'chirilmadi, nima qilaylik.")

# Barcha funksiyalarni ishga tushiramiz
if __name__ == "__main__":
    get_post()
    create_post()
    update_post()
    delete_post()