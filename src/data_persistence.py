import json, os
from .task import Task, DueDateTask, PriorityTask

class DataPersistence:
    def __init__(self, data_file="data/tasks.json"):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.path = os.path.join(root, data_file)

    def load_tasks(self):
        if not os.path.exists(self.path):
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            return []
        try:
            with open(self.path, encoding="utf-8") as f:
                rows = json.load(f)
            tasks = []
            for row in rows:
                row = dict(row)
                kind = row.pop("_type", "Task")
                row.setdefault("tags", [])
                cls = {"Task": Task, "DueDateTask": DueDateTask, "PriorityTask": PriorityTask}.get(kind, Task)
                tasks.append(cls(**row))
            return tasks
        except (ValueError, TypeError, json.JSONDecodeError) as e:
            print("Could not load tasks:", e)
            return []

    def save_tasks(self, tasks):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in tasks], f, indent=4, ensure_ascii=False)
