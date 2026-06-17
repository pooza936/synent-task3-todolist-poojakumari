import json
import os
from datetime import datetime

TODO_FILE = "todos.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def add_task(todos):
    task = input("\nEnter task: ").strip()
    if task:
        todos.append({
            "id": len(todos) + 1,
            "task": task,
            "done": False,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        save_todos(todos)
        print(f"✅ Task added: '{task}'")
    else:
        print("❌ Task cannot be empty!")

def view_tasks(todos):
    if not todos:
        print("\n📋 No tasks yet! Add one first.")
        return
    print("\n📋 YOUR TASKS:")
    print("-" * 45)
    for t in todos:
        status = "✅" if t["done"] else "⬜"
        print(f"  {t['id']}. {status} {t['task']}  [{t['created']}]")
    print("-" * 45)

def complete_task(todos):
    view_tasks(todos)
    try:
        num = int(input("\nEnter task number to mark complete: "))
        for t in todos:
            if t["id"] == num:
                t["done"] = True
                save_todos(todos)
                print(f"✅ Task '{t['task']}' marked as done!")
                return
        print("❌ Task not found!")
    except ValueError:
        print("❌ Please enter a valid number!")

def delete_task(todos):
    view_tasks(todos)
    try:
        num = int(input("\nEnter task number to delete: "))
        for t in todos:
            if t["id"] == num:
                todos.remove(t)
                save_todos(todos)
                print(f"🗑️  Task '{t['task']}' deleted!")
                return
        print("❌ Task not found!")
    except ValueError:
        print("❌ Please enter a valid number!")

def main():
    print("=" * 45)
    print("       📝 TODO LIST APP - by Kumar")
    print("=" * 45)

    todos = load_todos()

    while True:
        print("\n🔹 MENU:")
        print("  1. Add Task")
        print("  2. View Tasks")
        print("  3. Complete Task")
        print("  4. Delete Task")
        print("  5. Exit")

        choice = input("\nChoose option (1-5): ").strip()

        if choice == "1":
            add_task(todos)
        elif choice == "2":
            view_tasks(todos)
        elif choice == "3":
            complete_task(todos)
        elif choice == "4":
            delete_task(todos)
        elif choice == "5":
            print("\n👋 Goodbye! Stay productive!")
            break
        else:
            print("❌ Invalid choice! Please choose 1-5.")

if __name__ == "__main__":
    main()
