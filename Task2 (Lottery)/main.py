# Оголошуємо функцію, яка генерує випадкову послідовність унікальних
# чисел від min до max включно, з кількістю чисел = quantity
def get_numbers_ticker(min, max, quantity):
    # Імпортуємо функцію randint з модуля random
    from random import randint
    # Перевіряємо чи min, max, quantity є числами і їх корректність
    try:
        if min > max or quantity > (max - min +1):
            return []
    except TypeError:
        return []
    
    # Оголошуємо множину для зберігання унікальних чисел
    # та список для сортування чисел
    generated_sequence = set()
    sorted_sequence = []
    
    # Додаємо унікальні числа в множину допоки їх кількість не буде рівна quantity
    while len(generated_sequence) < quantity:
        generated_sequence.add(randint(min, max))
    # Сортуємо числа та повертаємо їх у вигляді списку
    sorted_sequence = sorted(generated_sequence)
    return list(sorted_sequence)