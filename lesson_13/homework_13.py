"""
++++++++++++++++++++++++++++++++++++++++++++++++
Декораторы в Python
++++++++++++++++++++++++++++++++++++++++++++++++
===============================================
1. Напишите декоратор uppercase_decorator, который делает результат выполнения функции прописными буквами.
Пример вызова:
@uppercase_decorator
def say_hello():
    return "hello, world!"
print(say_hello())  # "HELLO, WORLD!"
"""

# def uppercase_decorator(func):
#     def wrapper():
#         res = func().upper()
#         return res
#     return wrapper
#
# @uppercase_decorator
# def say_hello():
#     return 'hello, world!'
# print(say_hello())
"""
===============================================
2. Создайте декоратор repeat(n), который выполняет функцию n раз.
Пример вызова:
@repeat(3)
def hello():
    print("Hello!")
hello()
Вывод:
Hello!
Hello!
Hello!
"""
# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             for i in range(n):
#                 res = func()
#             return res
#         return wrapper
#     return decorator
#
# @repeat(3)
# def hello():
#     print('Hello!')
# hello()
"""
===============================================
3. Создайте декоратор cache, который кэширует результаты выполнения функции.
Если функция вызывается с теми же аргументами – возвращать сохраненный результат вместо нового вычисления.
Пример вызова:
@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b
print(slow_add(2, 3))  # "Вычисляю 2 + 3..." 5
print(slow_add(2, 3))  # 5 (результат взят из кэша)
"""
# def cache(func, cached = {}):
#     def wrapper(*args):
#         if args in cached:
#             return cached[args]
#         else:
#             res = func(*args)
#             cached[args] = res
#             return res
#     return wrapper
#
# @cache
# def slow_add(a, b):
#     print(f"Вычисляю {a} + {b}...")
#     return a + b
#
# print('первое', slow_add(2, 3))  # "Вычисляю 2 + 3..." 5
#
# print('второе', slow_add(2, 3))  # 5 (результат взят из кэша)

"""
===============================================
4. Создайте декоратор с таймером timer(repeat), который выполняет функцию repeat раз и выводит среднее время выполнения.
Пример вызова:
@timer(3)
def slow_function():
    time.sleep(1)
slow_function()  # Среднее время выполнения: 1.0002 сек
"""
# import time
#
#
# def timer(repeat):
#     avg_time = []
#     def decorator(func):
#         def wrapper(*args):
#             for i in range(repeat):
#                 start_time = time.time()
#                 res = func(*args)
#                 end_time = time.time()
#                 full_time = end_time - start_time
#                 avg_time.append(full_time)
#             print(f'Среднее время выполнения: {sum(avg_time) / repeat}')
#             return res
#         return wrapper
#     return decorator
#
#
# @timer(3)
# def slow_function():
#     time.sleep(1)
#
# slow_function()  # Среднее время выполнения: 1.0002 сек