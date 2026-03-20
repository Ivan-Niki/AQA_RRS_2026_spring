# ================= Домашнее задание (занятие 6) =================

# ----------------- Задание 1. Модуль. -------------------
# Перенесите ваши функции из прошлого домашнего задания в отдельный
# файл и импортируйте их в основной (исполняемый) файл.
# Запустите каждую вашу функцию по 1 или более раз в исполняемом файле.

from my_functions import sum_ignore_non_numbers, is_triangle, average, common_strings


# ---------- task_1 -----------
print(sum_ignore_non_numbers([1, 2, 3, 12.3, "Hello", False, 5.2])) # 23.5 (передаём список)
print(sum_ignore_non_numbers([1, 2, 'Hey', None, 4.3])) # 7.3 (передаём список)
print(sum_ignore_non_numbers((1, 2, 'Hey', None, 4.3, 2))) # 9.3 (передаём кортеж)


# ----------- task_2 -----------
print("Треугольник со сторонами 2, 4, 9:", is_triangle(2, 4, 9)) # False
print("Треугольник со сторонами 3, 4, 5:", is_triangle(3, 4, 5)) # True


# ----------- task_3 -----------
print(average(1, 2, 3, 4, 5, 6, 7, 8))
print(average())


# ----------- task_4 -----------
fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry', 'PiNeApple']
fruits_2 = ['Mango', 'apple', 'orange', 'cherry', 'PINEAPPLE']
print(common_strings(fruits_1, fruits_2, ignore_case=True))


# ----------------- Задание 2. Анонимная функция 🎭. -------------------
# Создайте анонимную функцию pow, которая принимает 2 аргумента x и y.
# Функция должна возвращать x, возведенное в степень y.
my_pow = lambda x, y: x ** y
print(my_pow(3, 2))


# ----------------- Задание 2. Змея 🐍. -------------------
# Создайте функцию snake_talk, которая принимает 1 аргумент text (строка).
# Функция должна создать новую строку, где все гласные буквы
# aeiouyAEIOUY в строке text дублируются.
# Например, такой вызовы функции snake_talk("Harry") должен вернуть
# строку "Haarryy".

def snake_talk(text):
    res_text = ""
    for c in text:
        if c in "aeiouyAEIOUY":
            res_text += c
        res_text += c

    return res_text

print(snake_talk("Harry"))