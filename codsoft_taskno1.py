import os 
import json 

# creating file 
file_name = "todolist.json"

#task loading function
def load_tasks():
    if os.path.exists(file_name): 
        with open (file_name, "r") as file:
            return json.load(file)
    return []

# saving tasks 
def save_tasks(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file)

# funsiton to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✔" if task['done'] else "✗"
            print(f"{i}. [{status}] {task['task']}")

# Main program
def main():
    tasks = load_tasks()

    while True:

        print("\n=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input ("Enter Your Choice: ")

        if choice == "1":
            task = input( "inter task: ")
            tasks.append({"task":task, "done":False})
            save_tasks(tasks)
            print("✅ Task added!")
        
        elif choice == "2":
            display_tasks(tasks)
        
        elif choice == "3":
            num = int(input("enter task which is done: "))
            if 1<= num <= len(tasks):
                tasks[num - 1]['done'] = True
                save_tasks(tasks)
                print("✔ Task marked as done!")
            else:
                    print("❌ Invalid task number.")

        elif choice == "4":
            display_tasks(tasks)
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                del tasks[num - 1]
                save_tasks(tasks)
                print("❌ Task deleted!")
            else:
                print("❌ Invalid task number.")

        elif choice == "5":
                print("Exiting the To-Do List. Goodbye!")
                break
        else:
                print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()













































