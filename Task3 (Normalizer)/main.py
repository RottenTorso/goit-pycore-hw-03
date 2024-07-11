#Імпортуємо бібліотеку re для роботи з регулярними виразами
import re
#Створюємо функцію normalize_phone, яка приймає номер телефону
def normalize_phone(phone_number):
    #Використовуємо регулярний вираз для видалення всіх символів, окрім "+" і цифр
    cleaned_number = re.sub(r"[^+\d]", '', phone_number)
    #Перевіряємо чи номер починається з "0" і повертаємо номер з префіксом "+38"
    if cleaned_number.startswith('0'):
        return f'+38{cleaned_number}'
    #Перевіряємо чи номер починається з "38" і повертаємо номер з префіксом "+"
    elif cleaned_number.startswith('38'):
        return f'+{cleaned_number}'
    #Якщо номер починається з "+" повертаємо номер без змін
    else: 
        return cleaned_number

