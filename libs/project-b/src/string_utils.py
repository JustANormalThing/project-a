def reverse_string(value: str) -> str:
    """Возвращает строку в обратном порядке."""
    return value[::-1]


def is_palindrome(value: str) -> bool:
    """Проверяет, является ли строка палиндромом."""
    normalized = value.lower().replace(" ", "")
    return normalized == normalized[::-1]


def count_words(value: str) -> int:
    """Возвращает количество слов в строке."""
    return len(value.split())


def capitalize_words(value: str) -> str:
    """Делает первую букву каждого слова заглавной."""
    return value.title()


def remove_spaces(value: str) -> str:
    """Удаляет пробелы из строки."""
    return value.replace(" ", "")


def count_characters(value: str) -> int:
    """Возвращает количество символов в строке."""
    return len(value)
