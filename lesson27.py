# Omborxona mini-CLI
# products nomli dictionary orqali mahsulotlarni saqlash
# import logging

# logging.basicConfig(level=logging.DEBUG,
#                     filename='app.log',
#                     filemode='a',
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# logging.info('hello world')
# logging.debug('hello world')

products = {
    "coca-cola": {"narxi": 10000, "soni": 50},
    "pepsi": {"narxi": 9000, "soni": 30},
    "shokolad": {"narxi": 20000, "soni": 134},
    "pishiriq": {"narxi": 60000, "soni": 350}
}

def add_product():
    nom = input("Mahsulot nomi: ").strip().lower()
    try:
        narxi = int(input("Narxi (so'm): "))
        soni = int(input("Soni (dona): "))
    except ValueError:
        print("Son kiriting (0 dan katta)")
        return

    if narxi <= 0 or soni <= 0:
        print("Son kiriting (0 dan katta): ")
        return

    if nom in products:
        products[nom]["soni"] += soni
    else:
        products[nom] = {"narxi": narxi, "soni": soni}

    print(f"OK. {nom} yangilandi: {products[nom]}")


def remove_product():
    nom = input("Mahsulot nomi: ").strip().lower()
    if nom not in products:
        print("Mahsulot topilmadi")
        return

    try:
        miqdor = int(input("Qancha miqdor olib chiqilsin: "))
    except ValueError:
        print("Son kiriting (0 dan katta): ")
        return

    if miqdor <= 0:
        print("Son kiriting (0 dan katta)")
        return

    available = products[nom]["soni"]
    if available < miqdor:
        print(f"Zaxira yetarli emas. Mavjud: {available} dona, so'rov: {miqdor} dona")
    else:
        products[nom]["soni"] -= miqdor
        print(f"OK. Qoldi: {products[nom]['soni']} dona")


def show_products():
    if not products:
        print("Omborda mahsulot yo'q")
        return

    print("\nMahsulotlar ro'yxati:")
    print("Nomi | Narxi | Soni | Jami")
    print("-" * 40)
    for nom, data in products.items():
        narxi = data["narxi"]
        soni = data["soni"]
        jami = narxi * soni
        print(f"{nom} | {narxi} | {soni} | {jami}")
    print("-" * 40)


def main():
    while True:
        print("\nMENYU")
        print("1: Mahsulot qo'shish")
        print("2: Mahsulot olib chiqish")
        print("3: Mahsulotlar ro'yxati")
        print("0: Chiqish")

        tanlov = input("Tanlovingiz: ")

        if tanlov == "1":
            add_product()
        elif tanlov == "2":
            remove_product()
        elif tanlov == "3":
            show_products()
        elif tanlov == "0":
            print("Dastur yakunlandi. Rahmat.")
            break
        else:
            print("Bunday variant mavjud emas!")


if __name__ == "__main__":
    main()
