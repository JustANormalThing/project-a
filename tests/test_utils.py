from datetime import date

from src.date_utils import (
    add_days,
    days_between,
    format_date,
)
from src.string_utils import (
    capitalize_words,
    count_words,
    is_palindrome,
    reverse_string,
)


def test_format_date():
    value = date(2026, 9, 30)

    assert format_date(value) == "30.09.2026"


def test_days_between():
    first = date(2026, 9, 1)
    second = date(2026, 9, 10)

    assert days_between(first, second) == 9


def test_add_days():
    value = date(2026, 9, 30)

    assert add_days(value, 5) == date(2026, 10, 5)


def test_reverse_string():
    assert reverse_string("Python") == "nohtyP"


def test_is_palindrome():
    assert is_palindrome("А роза упала на лапу Азора") is True
    assert is_palindrome("Python") is False


def test_count_words():
    assert count_words("Hello world") == 2


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"

def test_is_weekend():
    from datetime import date
    from src.date_utils import is_weekend

    assert is_weekend(date(2026, 9, 26)) is True
    assert is_weekend(date(2026, 9, 28)) is False


def test_remove_spaces():
    from src.string_utils import remove_spaces

    assert remove_spaces("Hello World") == "HelloWorld"


def test_count_characters():
    from src.string_utils import count_characters

    assert count_characters("Hello") == 5
