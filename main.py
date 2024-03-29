"""

1) Преобразовать в верхний регистр текст которую возвращает функция
 не изменяя код фунции применяя декоратор
"""

# def make_to_upper_text(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper


# @make_to_upper_text
# def get_text():
#     return 'hello world!'

# print(get_text())


"""
2) Функция get_number возврощает номер телефона  ‘996700123456’ применяя 
декоратор зашифруйте номер телефона так, чтобы остались только последние 
2 числа: (###########56), а остальные все были заменены на символ #.
"""

# def cipher_number(func):
#     def wrapper():
#         phone_number = func()
#         cipher_num = ''
#         for i, p in enumerate(phone_number):
#             if i in (0, 1, 2):
#                 cipher_num += p
#             elif i in (10, 11):
#                 cipher_num += p
#             else:
#                 cipher_num += '#'     

#         return cipher_num
#     return wrapper       


# @cipher_number
# def get_number():
#     return '996700123456'


# print(get_number())


"""
3) Напишите декоратор, выводящий приветствие перед выполнением функции
"""

# def greeting(func):
#     def wrapper():
#         print('Привет, сейчас я буду покажу номер телфона')
#         result = func()

#         return result
#     return wrapper


# @greeting
# def get_number():
#     return '996700123456'


# print(get_number())


"""
4) Напишите декоратор, удваивающий результат функции:
"""

# def double_salary(func):
#     def wrapper():
#         result = func()
#         return result * 2

#     return wrapper


# @double_salary
# def get_salary():
#     salary = 50000
#     return salary


# print(get_salary())


"""
5) Декоратор, печатающий сообщение после выполнения функции
"""

# def print_notification(func):
#     def wrapper():
#         result = func()
#         print('Функция выполнилась')
#         print(f'Вам начислили зарплату на сумму: {result}')

#         return result
#     return wrapper


# @print_notification
# def get_salary():
#     salary = 50000
#     return salary


# get_salary()


"""
1) Декоратор для измерения времени выполнения функции:
Напишите декоратор, который измеряет время выполнения функции и 
выводит результат.
"""

# import time


# def timer_decorator(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(f'Функция отправки сообщении пользавателям заняло:\n \
#                 {end_time - start_time:.2f} секунд')

#     return wrapper


# @timer_decorator
# def send_message_to_users():
#     users = range(1, 1000001)

#     for user in users:
#         print(f'Отправка сообщения пользователю {user}')


# send_message_to_users()