import os
import json
import argparse

'''
项目介绍：一个通过 CLI 控制的 ToDo List 工具，用户在终端输入命令，程序把任务保存到一个 json 文件中。
主要功能：
- 读取任务：从 json 文件中加载任务列表，并转换成 python 数据
- 保存任务：把当前任务列表写回 json 文件中
- 添加任务：把新任务加入列表，并保存到 json 文件中
- 列出任务：显示当前所有任务
- 删除任务：根据任务编号删除任务
- 标记完成：根据任务编号标记任务
- 搜索任务：根据关键字搜索任务并打印
- 清空已完成任务：删除所有已完成任务
'''

TODO_FILE = "tasks_fork.json"


def load_tasks():
    # 若文件存在则读取，否则返回空列表
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    # 保存当前任务，并缩进
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, description, priority='Medium'):
    # 添加任务，并保存到 json 文件中
    tasks.append({
        'description': description,
        'done': False,
        'priority': priority,
    })
    save_tasks(tasks)
    print(f"Added: {description}\tPriority: {priority}")


def list_task(tasks):
    # 罗列当前任务并显示完成标记
    if not tasks:
        print("No tasks.")
        return

    print("index\tstatus\tdescription\tpriority")
    for i, task in enumerate(tasks):
        status = "✅" if task['done'] == True else "❎"
        priority = task.get('priority', 'Medium')
        print(f"{i+1}.\t{status}\t{task['description']}\t\t{priority}")


def delete_task(tasks, index):
    # 按照索引删除任务，并检查索引是否合法，打印删除的任务
    if not tasks:
        print("No tasks.")
        return

    try:
        task_index = int(index)-1
        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task index.")
        else:
            removed = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"Removed: {removed['description']}")
    except ValueError:
        print("Invalid input.")


def mark_done(tasks, index):
    # 按照索引标记已完成任务
    if not tasks:
        print("No tasks.")
        return

    try:
        task_index = int(index)-1
        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task index.")
        else:
            tasks[task_index]['done'] = True
            save_tasks(tasks)
            print(f"Marked ✅ {tasks[task_index]['description']}")

    except ValueError:
        print("Invalid input.")


def search_task(tasks, keyword):
    # 按照关键字搜索任务
    if not tasks:
        print("No tasks.")
        return

    results = [task for task in tasks if keyword.lower()
               in task['description'].lower()]

    if not results:
        print("No matching task found.")
    else:
        for i, task in enumerate(results):
            status = "✅" if task['done'] == True else "❎"
            print(
                f"{i+1}.\t{status}\t{task['description']}\t{task['priority']}")


def clear_completed(tasks):
    # 删除已完成任务
    if not tasks:
        print("No tasks.")
        return

    tasks[:] = [task for task in tasks if not task['done']]
    save_tasks(tasks)
    print("Cleared all completed tasks.")


def empty_task(tasks):
    # 清空任务列表
    tasks.clear()
    save_tasks(tasks)
    print("Empty Succeeded!")


def main():
    # 交互式 cli
    tasks = load_tasks()
    print("Welcome to CLI TODO App")
    print("Commands")
    print('*'*33)
    print("*\tadd task priority\t*")
    print("*\tlist\t\t\t*")
    print("*\tdelete index\t\t\t*")
    print("*\tdone index\t\t\t*")
    print("*\tsearch keyword\t\t\t*")
    print("*\tclear\t\t\t*")

    print("*\tempty\t\t\t*")
    print("*\texit\t\t\t*")
    print('*'*33)

    while True:
        command = input("\n>").strip().split()
        if not command:
            continue

        if command[0] == "add" and len(command) > 1:
            if command[-1].capitalize() in ["High", "Medium", "Low"]:
                priority = command[-1].capitalize()
                description = " ".join(
                    command[1:-1]) if len(command) > 2 else " "
                if not description.strip():
                    print("Description cannot be empty.")
                    continue
                add_task(tasks, description, priority)
            else:
                description = " ".join(command[1:])
                add_task(tasks, description)

        elif command[0] == "list":
            list_task(tasks)

        elif command[0] == "delete" and len(command) == 2:
            delete_task(tasks, index=command[1])

        elif command[0] == "done" and len(command) == 2:
            mark_done(tasks, index=command[1])

        elif command[0] == "search" and len(command) > 1:
            keyword = " ".join(command[1:])
            search_task(tasks, keyword)

        elif command[0] == "clear":
            clear_completed(tasks)

        elif command[0] == "empty":
            empty_task(tasks)

        elif command[0] == "exit":
            print("Bye~")
            break

        else:
            print("Input Error, please try again.")


def cli_main():
    # 命令行参数式 cli
    tasks = load_tasks()

    parser = argparse.ArgumentParser(description="A simple CLI Todo App")

    parser.add_argument("command", choices=["add", "list", "delete", "done",
                        "search", "clear", "empty"], help="Command to run")

    parser.add_argument("value", nargs='*',
                        help="Task description, index, or search keyword")

    parser.add_argument(
        "--p", choices=["High", "Medium", "Low"], default="Medium", help="Priority of the task")

    args = parser.parse_args()

    if args.command == "add":
        if not args.value:
            print("Task description cannot be empty.")
            return
        description = " ".join(args.value)
        add_task(tasks, description, priority=args.p)

    elif args.command == "list":
        list_task(tasks)

    elif args.command == "delete":
        if len(args.value) != 1:
            print("Please provide exactly one index.")
            return
        delete_task(tasks, index=args.value[0])

    elif args.command == "done":
        if len(args.value) != 1:
            print("Please provide exactly one index.")
            return
        mark_done(tasks, index=args.value[0])

    elif args.command == "search":
        if not args.value:
            print("Keyword cannot be empty.")
            return
        keyword = " ".join(args.value)
        search_task(tasks, keyword)

    elif args.command == "clear":
        clear_completed(tasks)

    elif args.command == "empty":
        empty_task(tasks)


if __name__ == "__main__":
    cli_main()
