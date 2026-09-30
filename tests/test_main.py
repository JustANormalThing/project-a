from src.models import Task
from src.utils import complete_task, create_task


def test_create_task():
    task = create_task(1, "Test task")

    assert task.id == 1
    assert task.title == "Test task"
    assert task.completed is False


def test_complete_task():
    task = Task(1, "Test task")

    complete_task(task)

    assert task.completed is True
