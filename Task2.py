import re
import random

def get_numbers_ticket(min, max, quantity):
    min_max_range = range(min, max)
    rand_numb = random.sample(min_max_range, quantity)
    return rand_numb

number_regex = re.compile(r'^(?:[1-9]|[1-9][0-9]|[1-9][0-9][0-9]|1000)$')

def validate_number(check):
    return bool(number_regex.match(str(check)))

while True:
    min_str = input("Введіть мінімальне число рандому (від 1 до 1000): ")
    max_str = input("Введіть максимальне число рандому (від 1 до 1000): ")
    quantity_str = input("Введіть кількість рандомних чисел: ")
    
    if validate_number(min_str) and validate_number(max_str) and validate_number(quantity_str):
        min = int(min_str)
        max = int(max_str)
        quantity = int(quantity_str)

        if min > max:
            print("Мінімальне число повинно бути менше або дорівнювати максимальному числу.")
            continue
        
        try:
            rand_list = get_numbers_ticket(min, max, quantity)
            print(f"Cписок рандомних чисел: {rand_list}")
        except ValueError as e:
            print(f"Помилка: {e}. Можливо, кількість чисел занадто велика для даного діапазону.")
    else:
        print("Не вірний формат. Спробуйте знову.")


        