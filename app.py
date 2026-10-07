from flask import Flask, render_template, request, redirect, url_for
from project_b_utils import get_current_date, reverse_string,capitalize_text, load_tasks, save_tasks,get_logger



app = Flask(__name__)

logger = get_logger()

TASKS_FILE = "tasks.json"


@app.route("/")
def index():
    tasks = load_tasks(TASKS_FILE)

    return render_template(
        "index.html",
        tasks=tasks,
        current_date=get_current_date(),
    )


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "")

    title = capitalize_text(title)

    if not title:
        return redirect(url_for("index"))

    tasks = load_tasks(TASKS_FILE)

    tasks.append({
        "title": title,
        "completed": False,
    })

    save_tasks(tasks, TASKS_FILE)

    logger.info("Добавлена задача: %s", title)

    return redirect(url_for("index"))


@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    tasks = load_tasks(TASKS_FILE)

    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True
        save_tasks(tasks, TASKS_FILE)

        logger.info("Задача %s выполнена", task_id)

    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks = load_tasks(TASKS_FILE)

    if 0 <= task_id < len(tasks):
        task = tasks.pop(task_id)

        save_tasks(tasks, TASKS_FILE)

        logger.info("Удалена задача: %s", task["title"])

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
