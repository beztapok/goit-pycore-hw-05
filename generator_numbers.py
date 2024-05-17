import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генератор, який ідентифікує та повертає всі дійсні числа у заданому тексті.
    Числа в тексті мають бути чітко відокремлені пробілами.
    
    Args:
    text (str): Текст, з якого потрібно витягнути числа.
    
    Yields:
    float: Дійсне число з тексту.
    """
    # Використання регулярного виразу для знаходження чисел, відокремлених пробілами
    pattern = r'\b\d+\.\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable) -> float:
    """
    Обчислює загальний дохід, сумуючи всі числа, знайдені у тексті з допомогою генератора.
    
    Args:
    text (str): Текст, що містить числові дані.
    func (Callable): Функція-генератор для ідентифікації та повернення чисел.
    
    Returns:
    float: Загальний дохід отриманий з чисел у тексті.
    """
    return sum(func(text))

# Приклад використання
if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income:.2f}")

