from src.models import Task


def create_task(task_id: int, title: str) -> Task:
    return Task(id=task_id, title=title)


def complete_task(task: Task) -> Task:
    task.complete()
    return task