# Normativ 1.16

import multiprocessing
import time

# Berilgan kod
def calculate_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"{num} sonining factoriali hisoblandi.")

if __name__ == "__main__":
    # Boshlanish vaqtini olamiz
    start = time.time()
    # Hisoblanadigan sonlar ro'yxati
    numbers = [50000, 60000, 70000, 80000, 90000]
    # Jarayonlar
    processes = []

    # Har bir son uchun alohida process
    for num in numbers:
        p = multiprocessing.Process(target=calculate_factorial, args=(num,))
        processes.append(p)

    # Ularni ishga tushiramiz
    for p in processes:
        p.start()
    # Jarayonlarning tugashini kutish
    for p in processes:
        p.join()
    # Tugash vaqtini o'lchash
    end = time.time()

    print(f"\nBarcha hisoblar {end - start:.2f} soniyada tugadi.") # : - formatlashish, 2 - faqat 2ta kasr, f - float, o'nli son
