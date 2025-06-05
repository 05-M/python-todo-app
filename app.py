import json

def save_tasks_to_file(fileName, tasks_list_to_save):
    try:
        with open(fileName,"w") as file:
            json.dump(tasks_list_to_save, file, indent=4)
        print(f"Tasks saved successfully to {fileName}.")
    except Exception as e:
        print(f"Error occurred while saving tasks to {fileName}: {e}")

def add_new_task(tasks_list, filename):
    new_task_description_input = input("Enter the task: ")
    new_task_dict = {
        "description": new_task_description_input,
        "done": False
        }
    tasks_list.append(new_task_dict)
    print("Task added successfully.")
    save_tasks_to_file(filename, tasks_list)

def view_tasks(tasks_list):
    if not tasks_list:
        print("No tasks available.")
    else:
        print("\nYour tasks:")
        for index, task_dict in enumerate(tasks_list, 1):
            status_mark = "[X]" if task_dict["done"] else "[]"
            print(f"{index}. {status_mark} {task_dict['description']}")

def delete_task(tasks_list, filename):
    if not tasks:
        print("No tasks available to delete.")
        return
    else:
        print("Your tasks:")
        view_tasks(tasks_list)
        try:
            task_number_to_delete_str = input("Enter the number of the task you want to delete: ")
            task_number_to_delete = int(task_number_to_delete_str)
        except ValueError:
            print("Invalid input. Please enter a number for the task.")
            return
        
        if task_number_to_delete < 1 or task_number_to_delete > len(tasks_list):
            print("Invalid task number. Please try again.")
            return
        else:
            index_to_delete = task_number_to_delete - 1
            task_name_to_be_deleted = tasks_list[index_to_delete] 
            del tasks_list[index_to_delete]           
            print(f"Task '{task_name_to_be_deleted}' deleted successfully.")
            save_tasks_to_file(filename, tasks_list)

def edit_task(tasks_list, filename):
    if not tasks:
        print("No tasks available to edit.")
        return            
    else:
        print("Your tasks:")
        view_tasks(tasks_list)
        try:
            task_number_to_edit_str = input("Enter the number of the task you want to edit: ")
            task_number_to_edit = int(task_number_to_edit_str)
        except ValueError:
            print("Invalid input. Please enter a number for the task.")
            return
        if(task_number_to_edit < 1 or task_number_to_edit> len(tasks_list)):
            print("Invalid task number. Please try again.")
            return
        else:
            index_to_edit = task_number_to_edit - 1
            update_task_description = input("Enter the new task description: ")
            tasks_list[index_to_edit]['description'] = update_task_description
            print(f"Task '{tasks_list[index_to_edit]['description']}' updated successfully.")
            save_tasks_to_file(filename, tasks_list)

def mark_task_as_done(tasks_list, filename):
    if not tasks:
        print("No tasks available to mark as done.")
        return
    else:
        print("Your tasks:")
        view_tasks(tasks_list)
        try:
            task_number_to_mark_done_str = input("Enter the number of the task you want to mark as done: ")
            task_number_to_mark_done = int(task_number_to_mark_done_str)
        except ValueError:
            print("Invalid input. Please enter a number for the task.")
            return

        if task_number_to_mark_done < 1 or task_number_to_mark_done > len(tasks_list):
            print("Invalid task number. Please try again.")
            return
        else:
            index_to_mark = task_number_to_mark_done - 1
            if tasks_list[index_to_mark]["done"]:
                print(f"Task '{tasks_list[index_to_mark]['description']}' is already marked as done.")
            else:
                tasks_list[index_to_mark]["done"] = True
                print(f"Task '{tasks_list[index_to_mark]['description']}' marked as done successfully.")
                save_tasks_to_file(filename, tasks_list)

TASKS_FILENAME = "tasks_data.json"
tasks = []
try:
    with open(TASKS_FILENAME,"r") as file:
        tasks = json.load(file)
        print(f"Tasks loaded successfully from {TASKS_FILENAME}.")
except FileNotFoundError:
    print(f"{TASKS_FILENAME} not found. Starting with an empty task list.")
    tasks = []
except json.JSONDecodeError:
    print(f"Error decoding JSON from {TASKS_FILENAME}. Starting with an empty task list.")
    tasks = []
except Exception as e:
    print(f"An error occurred while loading tasks: {e}")           


while True:
    print("\nChoose an option:")
    print("1.Add a task")
    print("2.View tasks")
    print("3.Delete a task")
    print("4.Edit the task")
    print("5.Mark task as done")
    print("6.Exit")
    choice = input("Enter your choice: ")
    
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if choice == 1:
        add_new_task(tasks, TASKS_FILENAME)
    elif choice == 2:
        view_tasks(tasks)
    elif choice == 3:
        delete_task(tasks, TASKS_FILENAME)
    elif choice == 4:
         edit_task(tasks, TASKS_FILENAME)
    elif choice==5:
        mark_task_as_done(tasks, TASKS_FILENAME)
    elif choice == 6:
        save_tasks_to_file(TASKS_FILENAME, tasks)
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
        break