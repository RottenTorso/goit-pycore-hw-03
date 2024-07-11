from datetime import datetime, timedelta

# Оголошуємо функцію для отримання списку користувачів, чиї дні народження наближаються
def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    today = datetime.today()  # Отримуємо поточну дату
    to_congratulate = []  # Ініціалізуємо список для зберігання інформації про привітання
    
    for each in users:  # Перебираємо кожного користувача в списку
        try:
            # Перетворюємо рядок дати народження на об'єкт datetime
            birthday_date = datetime.strptime(each['birthday'], '%Y.%m.%d')
            # Замінюємо рік на поточний для порівняння
            temp_date = birthday_date.replace(year=today.year)
        except ValueError:  # Якщо формат дати некоректний, виводимо повідомлення і пропускаємо користувача
            print(f'Invalid date format for {each["name"]}')
            continue
        
        # Рахуємо різницю в днях між поточною датою і датою народження
        delta_days = (temp_date - today).days
        # Перевіяємо, чи день народження в межах наступних 7 днів або сьогодні
        if -1 <= delta_days <= 6:
            congratulation_day = temp_date
            # Якщо день народження припадає на вихідні, переносимо привітання на понеділок
            if congratulation_day.weekday() == 5:
                congratulation_day += timedelta(days=2)
            elif congratulation_day.weekday() == 6:
                congratulation_day += timedelta(days=1)
            # Приводимо дату привітання у рядок
            congratulation_day_str = datetime.strftime(congratulation_day, '%Y.%m.%d')
            # Додаємо інформацію про привітання в список словників
            to_congratulate.append({"name": each['name'], "congratulation_date": congratulation_day_str})

    return to_congratulate  # Повертаємо список користувачів для привітання