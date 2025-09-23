# Uyga vazifa

# 1
def only_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg < 0:
                raise TypeError('Faqat musbat sonlar qabul qilinadi.')
            return func(arg)
        return func(*args, **kwargs)
    return wrapper

@only_positive
def square(num):
    return num ** 2

print(square(5))
print(square(-5))

# 2
from datetime import datetime

def time_restricted(start_hour, end_hour):
    def decorator(func):
        def wrapper(*args, **kwargs):
            now = datetime.now().hour
            if start_hour <= now <= end_hour:
                return func(*args, **kwargs)
            else:
                print(f"Funksiya faqat {start_hour}:00 dan {end_hour}:00 gacha ishlaydi. Hozir esa {now}:00")
                return func(*args, **kwargs)
        return wrapper
    return decorator

@time_restricted(9, 17)
def send_report():
    print("Hisobot muvaffaqiyatli yuborildi")

send_report()

def count_calls(func):
    calls = 0

    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f'{func.__name__} funksiyasi {calls} marta chaqirildi')
        return func(*args, **kwargs)
    return wrapper

@count_calls
def hello():
    print('Hello World!')

hello()
hello()
hello()


def admin_only(func):
    def wrapper(*args, **kwargs):
        role = kwargs.get('role')
        if role == 'admin':
            return func(*args, **kwargs)
        else:
            raise PermissionError(f"{role}ga o'chirishga ruxsat yo'q!")
    return wrapper

@admin_only
def delete_user(user_id, **kwargs):
    print(f"Foydalanuvchi {user_id} muvaffaqiyatli o'chirildi")

delete_user(101, role='admin')
delete_user(102, role='user')

# def call_limit(limit):
#     def decorator(func):
#         def wrapper(*args, **kwargs):

