import os

class TaskManager:
    def __init__(self):
        # Ensure task.txt exists
        self.task_file = 'task.txt'
        if not os.path.exists(self.task_file):
            with open(self.task_file, 'w') as f:
                f.write("")

    def add_task(self, task):
        try:
            with open(self.task_file, 'a') as f:
                f.write(task + "\n")
            print(f"✅ Task added: {task}")
        except Exception as e:
            print(f"❗ Error writing task: {e}")

    def view_tasks(self):
        try:
            if os.path.exists(self.task_file):
                with open(self.task_file, 'r') as f:
                    tasks = f.readlines()
                return tasks if tasks else ["No tasks available."]
            return ["No tasks available."]
        except Exception as e:
            print(f"❗ Error reading tasks: {e}")
            return ["Error fetching tasks."]
