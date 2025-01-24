class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Выполнено" if self.is_completed else "Не выполнено"
        return f"Описание: {self.description}, Срок выполнения: {self.deadline}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Задача '{description}' добавлена.")

    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return

        print("Текущие задачи:")
        for task in self.tasks:
            print(task)

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
            print(f"Задача '{self.tasks[index].description}' отмечена как выполненная.")
        else:
            print("Некорректный индекс задачи.")


# Пример использования TaskManager
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Купить продукты", "2025-12-02")
    manager.add_task("Сдать проект", "2025-12-05")
    manager.show_tasks()

    # Отметим первую задачу как выполненную
    manager.mark_task_as_completed(0)
    manager.show_tasks()