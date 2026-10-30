import datetime

class CLIInterface:
    def __init__(self, manager): self.manager = manager
    def show(self, tasks, title="Tasks"):
        print(f"\n--- {title} ---")
        if tasks:
            for task in tasks: print(task)
        else: print("No tasks found.")
    def tags(self):
        s = input("Tags (comma-separated, optional): ").strip()
        return [x.strip().lower() for x in s.split(",") if x.strip()]
    def run(self):
        while True:
            print("\n--- Enhanced Task Manager Menu ---")
            for line in ["1. Add Normal Task", "2. Add Due Date Task", "3. Add Priority Task", "4. List All Tasks", "5. Complete Task", "6. Delete Task", "7. Search Tasks", "8. Filter Tasks", "9. Sort Tasks", "0. Exit"]: print(line)
            choice = input("Enter your choice (0-9): ").strip()
            if choice in ["1", "2", "3"]:
                desc = input("Task description: ").strip()
                if not desc: print("Description cannot be empty."); continue
                if choice == "1": task = self.manager.add_normal_task(desc, self.tags())
                elif choice == "2":
                    date = input("Due date (YYYY-MM-DD): ").strip()
                    try: datetime.datetime.strptime(date, "%Y-%m-%d"); task = self.manager.add_due_date_task(desc, date, self.tags())
                    except ValueError: print("Invalid date."); continue
                else:
                    priority = input("Priority (High/Medium/Low): ").strip().capitalize()
                    task = self.manager.add_priority_task(desc, priority, self.tags())
                print(f"Task added with ID {task.id}." if task else "Invalid input.")
            elif choice == "4": self.show(self.manager.get_all_tasks(), "Your Tasks")
            elif choice in ["5", "6"]:
                try:
                    task_id = int(input("Task ID: "))
                    result = self.manager.complete_task(task_id) if choice == "5" else self.manager.delete_task(task_id)
                    print(result[1])
                except ValueError: print("Enter a valid number.")
            elif choice == "7":
                word = input("Search keyword: "); self.show(self.manager.search_tasks(word), "Search Results")
            elif choice == "8":
                status_text = input("Status (completed/pending/all): ").lower().strip()
                status = True if status_text == "completed" else False if status_text == "pending" else None
                before_text = input("Due before (YYYY-MM-DD, optional): ").strip()
                after_text = input("Due after (YYYY-MM-DD, optional): ").strip()
                priority = input("Priority (High/Medium/Low, optional): ").strip().capitalize()
                tags = [x.strip() for x in input("Tags (comma-separated, optional): ").split(",") if x.strip()]
                try:
                    before = datetime.datetime.strptime(before_text, "%Y-%m-%d").date() if before_text else None
                    after = datetime.datetime.strptime(after_text, "%Y-%m-%d").date() if after_text else None
                except ValueError: print("Invalid date."); continue
                if priority not in ["High", "Medium", "Low"]: priority = None
                self.show(self.manager.filter_tasks(status, before, after, priority, tags or None), "Filtered Tasks")
            elif choice == "9":
                criterion = input("Sort by (id/description/completed/due_date/priority): ").strip().lower() or "id"
                reverse = input("Descending? (yes/no): ").strip().lower() == "yes"
                self.show(self.manager.sort_tasks(criterion, reverse), "Sorted Tasks")
            elif choice == "0": print("Goodbye!"); break
            else: print("Invalid choice.")
