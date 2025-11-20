# Requests
from urllib.error import URLError

# valyuta
# response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
# print(response.json())
#
# for i in response.json()[0:3]:
#     name = i.get('CcyNm_UZ')
#     rate = i.get("Rate")
#     date = i.get("Date")
#     diff = i.get("Diff")
#     print(f'{name} - {rate}\nbugun {date}\n{diff}')

# Qidiruv parametrlari
# url = "https://en.wikipedia.org/w/api.php"
#
# param = {
#     "action" :"query",
#     "list" :"search",
#     "srsearch" :"Islam_Abdullaev",
#     "format" :"json"
# }
#
# # GET so'rovini yuborish
# response = requests.get(url, params=param)
#
# # JSON natijani chiqarish
# data = response.json()

# ---------------------------------------------------------------------------------------------
# import requests
#
# data = {
#     "name": {
#         "uz": "string",
#         "ru": "string",
#         "eng": "string"
#     },
#     "description": {
#         "uz": "string",
#         "ru": "string",
#         "eng": "string"
#     }
# }
# url_id = "https://staging.softtrans.uz/api/faq/test2/"
# response = requests.post(url_id, json=data)
# print(response.status_code)
# print(response.json())
#
# update_url = response.json().get('id')
# up_data = {
#     "name": {
#         "uz": "string2",
#         "ru": "string2",
#         "eng": "string2"
#     },
#     "description": {
#         "uz": "string2",
#         "ru": "string2",
#         "eng": "string2"
#     }
# }
# response = requests.put(url_id + f'{update_url}/', json=up_data)
# print(response.status_code)
# print(response.json())
#
# response = requests.get(url_id + f'{update_url}/')
# print(response.status_code)
# print(response.json())
#
# response = requests.delete(url_id + f'{update_url}/')
# print(response.status_code)

# ===========================================================================================





