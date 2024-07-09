import re

def normalize_phone(phone_number):
    format_for_number = re.sub(r'[^\d+]', '', phone_number)
    
    if format_for_number.startswith('+'):

        if format_for_number.startswith('+380'):
            pass
        else:
            format_for_number = format_for_number
    else:
        if format_for_number.startswith('380'):

            format_for_number = '+' + format_for_number
        else:
            format_for_number = '+38' + format_for_number

    return format_for_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)