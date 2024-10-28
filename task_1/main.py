
from typing import Callable
from collections import defaultdict


def caching_fibonacci() -> Callable[[int], int]:
    # Створити порожній словник cache
    cache = defaultdict()

    def fibonacci(n : int) -> int :
      
        if n <= 0 :
            return 0
        elif n ==1 :
            return 1
        else:
            # Використання рекурсії для обчислення чисел Фібоначчі.
            if n not in cache:
                # Якщо число не знаходиться у кеші, функція має обчислити його, зберегти у кеш та повернути результат.
                cache[n] = fibonacci(n-1) + fibonacci(n-2)
            return cache[n]
    
    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610