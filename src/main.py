from src.utils import create_task, complete_task


def main() -> None:
    task = create_task(1, "Изучить Git")
    print(f"Задача: {task.title}")
    print(f"Выполнена: {task.completed}")

    complete_task(task)

    print(f"Выполнена после завершения: {task.completed}")


if __name__ == "__main__":
    main()
