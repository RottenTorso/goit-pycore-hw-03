import datetime

# Оголошуємо функцію, яка приймає рядок з датою, 
# вираховує різницю в днях між датю і поточним днем 
# і повертає різницю цілим числом
def get_days_from_today(date: str) -> int:
    # Отримуємо поточну дату
    today_date = datetime.datetime.today()
    # Перевіряємо чи дата відповідає формату
    try:
        # Конвертуємо рядок в об'єкт дати з потрібним форматом
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        # Повертаємо повідомлення про некорректний формат дати
        return "Date format is incorrect. Please use YYYY-MM-DD"
    # Повертаємо різницю в днях
    return (today_date - date).days
