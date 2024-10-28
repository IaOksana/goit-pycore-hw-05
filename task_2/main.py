# Необхідно створити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати всі дійсні числа, 
# що вважаються частинами доходів, і повертати їх як генератор. Дійсні числа у тексті записані без помилок, 
# чітко відокремлені пробілами з обох боків. Також потрібно реалізувати функцію sum_profit, 
# яка буде використовувати generator_numbers для підсумовування цих чисел і обчислення загального прибутку.

from typing import Callable
import re


""""Функція generator_numbers(text: str) повинна приймати рядок як аргумент і повертати генератор, 
 що ітерує по всіх дійсних числах у тексті. 
 Дійсні числа у тексті вважаються записаними без помилок і чітко відокремлені пробілами з обох боків."""
def generator_numbers(text: str) -> float:

    # Регулярний вираз для ідентифікації дійсних чисел, відокремлених пробілами
    pattern = r'(?<!\S)[+-]?\d+(\.\d+)?(?!\S)'

    # Пошук дійсних чисел у тексті
    for match in re.finditer(pattern, text):
        yield float(match.group()) 


""" Функція sum_profit(text: str, func: Callable) має використовувати генератор generator_numbers 
 для обчислення загальної суми чисел у вхідному рядку та приймати його як аргумент при виклику."""
def sum_profit(text: str, func: Callable) -> float:
    total_profit = 0.0
    gen = generator_numbers(text)
    
    for number in gen:
        total_profit += number
    
    return total_profit


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")