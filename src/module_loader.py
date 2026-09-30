import sys
import os

# Добавляем путь к исходному коду Проекта Б
sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(__file__),
        "../libs/project-b/src"
    )
)

from date_utils import get_current_date, format_date,is_weekend
from string_utils import reverse_string, capitalize_words,remove_spaces


def main():
    print(f"Текущая дата: {get_current_date()}")
    print(f"Обратный текст: {reverse_string('Hello World')}")
    print(
        f"С заглавной: "
        f"{capitalize_words('hello world from project a')}"
    )
    print(f"Выходной день: {is_weekend(get_current_date())}")
    print(f"Без пробелов: {remove_spaces('Hello World')}")



if __name__ == "__main__":
    main()
