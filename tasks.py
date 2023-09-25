"""
    Crea una aplicación de lista de tareas usando clases en Python.
    La aplicación debe permitir agregar tareas, marcar tareas como completadas y ver la lista de tareas.

"""
import random


class Tasks:
    def __init__(self):
        self.tasks = []

    def get_tasks(self):
        return self.tasks

    def add_task(self, title, description, id):
        task = {
            "id": id,
            "title": title,
            "description": description,
            "is_completed": False
        }
        self._add_task_to_taks(task)
        print(f"Tarea agregada con el id: {task['id']}")

    def complete_task_by_id(self, id):
        for task in  self.tasks:
            if task["id"] == id:
                task["is_completed"] = True
                print("Tarea completada")
                return True


    def _generate_id(self):
        return random.randint(1, 99)

    def _add_task_to_taks(self, task):
        self.tasks.append(task)



tasks = Tasks()


print(tasks.get_tasks())
tasks.add_task("Aprender clases", "aprender sobre clases en python", 1)
tasks.add_task("Aprender funciones", "aprender sobre funciones en python", 2)
print(tasks.get_tasks())
tasks.complete_task_by_id(1)
print(tasks.get_tasks())
