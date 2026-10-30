import datetime
from .task import Task, DueDateTask, PriorityTask
from .data_persistence import DataPersistence

class TaskManager:
    PRIORITY_MAP = {"High": 1, "Medium": 2, "Low": 3}
    def __init__(self, data_file="data/tasks.json"):
        self.persistence = DataPersistence(data_file)
        self.tasks = self.persistence.load_tasks()
        self.next_id = max((t.id for t in self.tasks), default=0) + 1
    def save(self): self.persistence.save_tasks(self.tasks)
    def add_normal_task(self, description, tags=None):
        t = Task(self.next_id, description, tags=tags); self.tasks.append(t); self.next_id += 1; self.save(); return t
    def add_due_date_task(self, description, due_date, tags=None):
        try: t = DueDateTask(self.next_id, description, due_date, tags=tags)
        except ValueError: return None
        self.tasks.append(t); self.next_id += 1; self.save(); return t
    def add_priority_task(self, description, priority, tags=None):
        try: t = PriorityTask(self.next_id, description, priority, tags=tags)
        except ValueError: return None
        self.tasks.append(t); self.next_id += 1; self.save(); return t
    def get_all_tasks(self): return list(self.tasks)
    def complete_task(self, task_id):
        t = next((x for x in self.tasks if x.id == task_id), None)
        if not t: return False, "Task not found."
        if t.completed: return False, "Task is already completed."
        t.mark_complete(); self.save(); return True, "Task marked as completed."
    def delete_task(self, task_id):
        t = next((x for x in self.tasks if x.id == task_id), None)
        if not t: return False, "Task not found."
        self.tasks.remove(t); self.save(); return True, "Task deleted successfully."
    def search_tasks(self, keyword):
        k = keyword.strip().lower()
        return [t for t in self.tasks if k and (k in t.description.lower() or any(k in tag.lower() for tag in t.tags))]
    def filter_tasks(self, status=None, due_date_before=None, due_date_after=None, priority_level=None, contains_tags=None):
        result = self.tasks
        if status is not None: result = [t for t in result if t.completed == status]
        if due_date_before is not None: result = [t for t in result if isinstance(t, DueDateTask) and t.due_date <= due_date_before]
        if due_date_after is not None: result = [t for t in result if isinstance(t, DueDateTask) and t.due_date >= due_date_after]
        if priority_level: result = [t for t in result if isinstance(t, PriorityTask) and t.priority == priority_level]
        if contains_tags:
            wanted = [x.lower() for x in contains_tags]
            result = [t for t in result if all(x in [tag.lower() for tag in t.tags] for x in wanted)]
        return list(result)
    def sort_tasks(self, criterion="id", reverse=False):
        def key(t):
            if criterion == "description": return t.description.lower()
            if criterion == "completed": return t.completed
            if criterion == "due_date": return (t.due_date if isinstance(t, DueDateTask) else datetime.date.max, t.id)
            if criterion == "priority": return (self.PRIORITY_MAP.get(t.priority, 99) if isinstance(t, PriorityTask) else 99, t.id)
            return t.id
        return sorted(self.tasks, key=key, reverse=reverse)
