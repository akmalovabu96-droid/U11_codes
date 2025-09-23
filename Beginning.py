# Yakuniy normativ

# a) Talabalar va baholar lug'ati
talaba_baholari = {
    "Ali": {"Matematika": 5, "Ingliz tili": 4},
    "Vali": {"Matematika": 4, "Ingliz tili": 3},
    "Zuhra": {"Matematika": 5, "Ingliz tili": 5},
    "Olim": {"Matematika": 3, "Ingliz tili": 4}
}

# b) Yangi talaba qo‘shish
talaba_baholari["Anvar"] = {"Matematika": 4, "Ingliz tili": 3}

# c) Talabani o‘chirish (pop bilan)
olib_tashlangan = talaba_baholari.pop("Ali")
print("Ali lug‘atdan o‘chirildi:", olib_tashlangan)

# Izoh:
# del talaba_baholari["Ali"]  # Faqat o‘chiradi, qiymatini qaytarmaydi
# pop esa o‘chiradi va o‘sha qiymatni qaytara oladi

print("-" * 20)

# d) Har bir talabaning baholarini chiqarish
for talaba, fanlar in talaba_baholari.items():
    print(f"{talaba}ning baholari:")
    for fan, baho in fanlar.items(): # items metodi har bir elementni juftlik ko'rinishida qaytaradi
        print(f"  {fan}: {baho}")

print("-" * 20)

# e) Bahoni o‘zgartirish (masalan Anvarning Ingliz tili bahosi 3 -> 2 bo‘lsin)
talaba_baholari["Anvar"]["Ingliz tili"] = 2

# Yangilangan baholarni chiqarish
for talaba, fanlar in talaba_baholari.items():
    print(f"{talaba}ning yangilangan baholari:")
    for fan, baho in fanlar.items():
        print(f"  {fan}: {baho}")

print("-" * 20)

# f) Yangi dict – o‘rtacha baholar
ortacha_baholar = {}
for talaba, fanlar in talaba_baholari.items():
    baholar = fanlar.values() # lug'atdagi faqat sonlarni(baholarni) ajratib oladi
    ortacha = sum(baholar) / len(baholar)
    ortacha_baholar[talaba] = ortacha

print("Talabalarning o‘rtacha baholari:", ortacha_baholar)

print("-" * 20)

# g) O‘rtacha bahosi 3 dan kichik bo‘lganlar
for talaba, ortacha in ortacha_baholar.items():
    if ortacha < 3:
        print(f"{talaba}, yiqildingiz.")