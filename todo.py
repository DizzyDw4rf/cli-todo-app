import json
import os
import sys
from datetime import datetime


TASK_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task {task_id} has been added: {description}.')

def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} updated: {description}')
            return
    print(f'Task {task_id}: can not be found!')

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f'Task {task_id}: deleted successfully')

def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            if task['status'] != 'done':
                task['status'] = 'in-progress'
                task['updatedAt'] = datetime.now().isoformat()
                save_tasks(tasks)
                print(f'Task {task_id}: Marked as in-progress.')
                return
            print(f'Task {task_id}: Marked as "done" already!')
            return
    print(f'Task {task_id}: Not found')

def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            if task['status'] != 'done':
                task['status'] = 'done'
                task['updatedAt'] = datetime.now().isoformat()
                save_tasks(tasks)
                print(f'Task {task_id}: Marked as done.')
                return
            print(f'Task {task_id}: Marked as "done" already')
            return
    print(f'Task {task_id}: Not found')

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print('No tasks available')
        return
    else:
        for task in tasks:
            print(f'ID: {task['id']}, Description: {task['description']}, Status: {task['status']},'
                  f'Created At: {task['createdAt']}, Updated At: {task['updatedAt']}')
def list_todo():
    tasks = load_tasks()
    todo_tasks = [task for task in tasks if task['status'] == 'todo']
    if not todo_tasks:
        print('No tasks marked as "todo"')
        return
    else:
        for task in todo_tasks:
            print(f'ID: {task['id']}, Description: {task['description']}, Status: {task['status']},'
                  f'Created At: {task['createdAt']}, Updated At: {task['updatedAt']}')

def list_in_progress():
    tasks = load_tasks()
    in_progress_tasks = [task for task in tasks if task['status'] == 'in-progress']
    if not in_progress_tasks:
        print('No tasks marked as "in-progress"')
        return
    else:
        for task in in_progress_tasks:
            print(f'ID: {task['id']}, Description: {task['description']}, Status: {task['status']},'
                  f'Created At: {task['createdAt']}, Updated At: {task['updatedAt']}')

def list_done():
    tasks = load_tasks()
    done_tasks = [task for task in tasks if task['status'] == 'done']
    if not done_tasks:
        print('No tasks marked as "done"')
        return
    else:
        for task in done_tasks:
            print(f'ID: {task['id']}, Description: {task['description']}, Status: {task['status']},'
                  f'Created At: {task['createdAt']}, Updated At: {task['updatedAt']}')

def main():
    if len(sys.argv) < 2:
        print('Usage: python todo.py <action> [arguments]')
        return

    action = sys.argv[1]

    if action == 'add' and len(sys.argv) > 2:
        description = " ".join(sys.argv[2:])
        add_task(description)
    elif action == 'update' and len(sys.argv) > 3:
        task_id = int(sys.argv[2])
        description = " ".join(sys.argv[3:])
        update_task(task_id, description)
    elif action == 'delete' and len(sys.argv) > 2:
        task_id = int(sys.argv[2])
        delete_task(task_id)
    elif action == 'in-progress' and len(sys.argv) > 2:
        task_id = int(sys.argv[2])
        mark_in_progress(task_id)
    elif action == 'done' and len(sys.argv) > 2:
        task_id = int(sys.argv[2])
        mark_done(task_id)
    elif action == 'list':
        list_tasks()
    elif action == 'list-todo':
        list_todo()
    elif action == 'list-in-progress':
        list_in_progress()
    elif action == 'list-done':
        list_done()
    else:
        print('Invalid action or argument. Usage:')
        print(' add <description>')
        print(' update <task_id> <description>')
        print(' delete <task_id>')
        print(' in-progress <task_id>')
        print(' done <task_id>')
        print(' list')
        print(' list-todo')
        print(' list-in-progress')
        print(' list-done')

if __name__ == '__main__':
    main()
