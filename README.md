# Todo App CLI

[English](./README.md) | [中文](./README.zh-CN.md)

A simple command-line ToDo List application built with Python.

This project allows users to manage tasks directly from the terminal. Tasks are stored locally in a JSON file, so the data will still be available after the program exits.

## Project Overview

This is a beginner-friendly Python project designed to practice core Python skills, including:

- Command-line argument parsing with `argparse`
- File reading and writing
- JSON data storage
- Functions and modular logic
- Lists and dictionaries
- Error handling
- Basic CLI application design

## Features

- Add a new task
- Set task priority: `High`, `Medium`, or `Low`
- List all tasks
- Mark a task as completed
- Delete a task by index
- Search tasks by keyword
- Clear all completed tasks
- Empty the entire task list
- Save tasks automatically to a local JSON file

## Technologies Used

- Python 3
- `argparse`
- `json`
- `os`

No third-party packages are required.

## Project Structure

```text
todo-cli-app/
│
├── todo_cli.py
├── tasks.json
└── README.md
```

## How to Run

First, make sure you are in the project folder:

```bash
cd todo-cli-app
```

Then run commands using:

```bash
python3 todo_cli.py <command>
```

## Commands

### Add a task

```bash
python3 todo_cli.py add learn python argparse
```

Add a task with priority:

```bash
python3 todo_cli.py add learn python argparse --priority High
```

Available priority values:

```text
High
Medium
Low
```

If no priority is provided, the default priority is `Medium`.

### List all tasks

```bash
python3 todo_cli.py list
```

Example output:

```text
index   status  description             priority
1.      ❎      learn python argparse    High
2.      ✅      review json              Medium
```

### Mark a task as done

```bash
python3 todo_cli.py done 1
```

This marks task number `1` as completed.

### Delete a task

```bash
python3 todo_cli.py delete 1
```

This deletes task number `1`.

### Search tasks

```bash
python3 todo_cli.py search python
```

This searches for tasks that contain the keyword `python`.

### Clear completed tasks

```bash
python3 todo_cli.py clear
```

This removes all tasks that have already been marked as completed.

### Empty all tasks

```bash
python3 todo_cli.py empty
```

This clears the entire task list.

## Data Storage

Tasks are saved in a local JSON file:

```text
tasks.json
```

Each task is stored as a dictionary with the following structure:

```json
{
  "description": "learn python argparse",
  "done": false,
  "priority": "High"
}
```

## Example Workflow

```bash
python3 todo_cli.py add learn python functions --priority High
python3 todo_cli.py add practice json file storage
python3 todo_cli.py list
python3 todo_cli.py done 1
python3 todo_cli.py search python
python3 todo_cli.py clear
python3 todo_cli.py list
```

## What I Learned

Through this project, I practiced several important Python fundamentals:

- How to use `argparse` to build a command-line tool
- How to store and load data with JSON
- How to use functions to separate program logic
- How to handle user input and invalid values
- How to work with lists and dictionaries
- How to build a small but practical Python application

This project also helped me understand basic task management logic, which is useful preparation for future AI agent projects where an agent may need to create, manage, and track tasks.

## Future Improvements

Possible improvements include:

- Add task deadlines
- Sort tasks by priority
- Filter tasks by status
- Add task categories
- Improve error handling for broken JSON files
- Split the project into multiple files
- Support both interactive CLI mode and command-line argument mode
