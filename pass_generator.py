import random
import sys

# Задаем необходимые символы
low_case = "qwertyuiopasdfghjklzxcvbnm"
up_case = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "123456789"
symbols = "@#$%&\/?!"

# Объединяем символы в use_for
use_for = low_case + up_case + numbers + symbols
print("Введите название для пароля: ")

# Пользователь вводит название, для чего будет сгенерирован пароль
name_for_pass = input()
print("Количество символов: ")

# Пользователь вводит количество символов, необходимое для пароля
length_for_pass = (int(input()))

# Генерация пароля с использованием символов и длины массива, которое ввёл пользователь
password = "".join(random.sample(use_for, length_for_pass))

# Сохранение пароля в файл passwords.txt
original_stdout = sys.stdout

with open('passwords.txt', 'a') as f:
    sys.stdout = f
    print(name_for_pass, ": ",  password)
    sys.stdout = original_stdout
