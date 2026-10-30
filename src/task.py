import datetime

class Task:
    def __init__(self, id, description, completed=False, tags=None):
        self.id = id
        self.description = description
        self.completed = completed
        self.tags = list(tags) if tags is not None else []

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {"id": self.id, "description": self.description, "completed": self.completed, "tags": self.tags, "_type": "Task"}

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        tags = f" | Tags: {', '.join(self.tags)}" if self.tags else ""
        return f"ID: {self.id} | Description: {self.description} | Status: {status}{tags}"

class DueDateTask(Task):
    def __init__(self, id, description, due_date, completed=False, tags=None):
        super().__init__(id, description, completed, tags)
        self.due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date() if isinstance(due_date, str) else due_date

    def to_dict(self):
        data = super().to_dict()
        data.update({"due_date": self.due_date.strftime("%Y-%m-%d"), "_type": "DueDateTask"})
        return data

    def __str__(self):
        return f"{super().__str__()} | Due: {self.due_date:%Y-%m-%d}"

class PriorityTask(Task):
    def __init__(self, id, description, priority, completed=False, tags=None):
        super().__init__(id, description, completed, tags)
        if priority not in ["High", "Medium", "Low"]:
            raise ValueError("Priority must be High, Medium, or Low")
        self.priority = priority

    def to_dict(self):
        data = super().to_dict()
        data.update({"priority": self.priority, "_type": "PriorityTask"})
        return data

    def __str__(self):
        return f"{super().__str__()} | Priority: {self.priority}"
