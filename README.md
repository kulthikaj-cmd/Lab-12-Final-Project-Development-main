# Final Project: Enhanced Task Manager CLI

A Python command-line task manager demonstrating OOP, modular design, JSON persistence, search, filtering, and sorting.

## Features
- Normal tasks, due-date tasks, and priority tasks
- Optional tags
- List, complete, and delete tasks
- Case-insensitive partial search in descriptions and tags
- Filter by completion status, due-date range, priority, and tags
- Sort by ID, description, completion status, due date, and priority
- Automatically saves data in `data/tasks.json`

## Run
Requires Python 3.10 or newer. No external packages are needed.

```bash
python main.py
```

## Structure
- `src/task.py`: Task classes
- `src/data_persistence.py`: JSON loading and saving
- `src/task_manager.py`: CRUD, search, filter, and sort logic
- `src/cli_interface.py`: Command-line menu
- `main.py`: Program entry point
- `data/tasks.json`: Saved tasks

## Demo
Add one normal task tagged `study,urgent`, one due-date task, and one High-priority task. Then demonstrate list, search, filter, sort, complete, delete, and restart the program to show saved data.
