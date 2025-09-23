# for i in range(10):
#     print(i)

# try:
#     print(1/0)
# except ZeroDivisionError:
#     print("You can't divide by zero")

sonlar = [1, 4, 7, 10] # 22
yigindi = 0
for x in sonlar:
    yigindi += x
print("Elementlar yig'indisi:", yigindi)

# Big O
teskari = []
for index, i in enumerate(sonlar):
    print(index, i)
    teskari.append(sonlar[len(sonlar)-index-1])
    print(teskari)