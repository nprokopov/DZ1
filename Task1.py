from datetime import datetime
import re 

current_date = datetime.now()

date_regex = re.compile(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$')

def validate_date(date):
    if date_regex.match(date):
        return True
    else:
        return False

while True:
    input_date = input("Введіть дату: (yyyy-mm-dd)\n")

    if validate_date(input_date):
        input_date = datetime.strptime(input_date, '%Y-%m-%d').date()

        difference = current_date.toordinal() - input_date.toordinal()

        print(f"Різниця: {difference} днів.")
    else:
        print("Не вірний формат дати. Повторіть.")