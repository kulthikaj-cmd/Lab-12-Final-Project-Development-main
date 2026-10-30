# Project Plan: Enhanced Task Manager CLI

## Introduction
A command-line application for organizing tasks, deadlines, and priorities using Python OOP and modular design.

## Functional Requirements
- Create normal, due-date, and priority tasks.
- Add tags to tasks.
- List, complete, and delete tasks.
- Search descriptions and tags using case-insensitive partial matching.
- Filter by completion status, due-date range, priority, and tags.
- Sort by ID, description, completion status, due date, and priority.
- Persist tasks in JSON format.

## Module Design
- `task.py`: Defines Task, DueDateTask, and PriorityTask.
- `data_persistence.py`: Loads and saves JSON records.
- `task_manager.py`: Implements task operations and data manipulation.
- `cli_interface.py`: Handles menus and user input/output.
- `main.py`: Starts the application.

## Testing Plan
1. Add each task type and check the displayed fields.
2. Add tags and search by a partial word or tag.
3. Complete and delete tasks by ID.
4. Combine status, date, priority, and tag filters.
5. Test all sorting criteria in ascending and descending order.
6. Restart the application and confirm that tasks persist.
7. Try invalid dates, priorities, IDs, and menu options.

## Implementation Challenges
Date filtering requires comparing `datetime.date` objects. Sorting mixed task types requires fallback sort keys for tasks without due dates or priority. Separating models, persistence, business logic, and CLI makes the project easier to debug and maintain.

## Future Work
A GUI, SQLite database, reminders, recurring tasks, user accounts, and automated unit tests could be added later.
