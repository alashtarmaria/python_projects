# 1 - add tasks to a list
# 2 - mark task as complete
# 3 - view tasks
# 4 - Quit

tasks = []

def main():
    message = """
1 - add tasks to a list
2 - mark task as complete
3 - view tasks
4 - Quit"""

    while True:
      print(message)
      choice = input("Enter your choice :")

      if choice == "1":
       # add tasks to a list 
         add_tasks()

      elif choice == "2" :
          mark_task_completed()
  
      elif choice == "3":
          view_tasks()

      elif choice == "4":
          break


def add_tasks():
    # get task from user 
    task = input("Please Enter Task :")
    # task status
    task_status ={"task" :task , "completed":False }
    # add task to task lists
    tasks.append(task_status)
    

def mark_task_completed():

    # get list of incomplete tasks
    incomplete_tasks = [task for task in tasks if task["completed"]== False]
    
    if not incomplete_tasks:
        print("No tasks to mark as complete")
        return
    
    # show tasks to the user
    for index, task in enumerate(incomplete_tasks):
        print(f"{index+1}- {task['task']}")
        print("-"*30)


    # get the task from the user
    task_number = int(input("Choose the task number to complete :"))

    # mark the task as completed
    # user will enter a number that starts from one but index starts from 0 so ww will take it as  : task_number - 1 
    incomplete_tasks[task_number - 1]["completed"] = True

    
    # print message
    print("Task marked completed")

def view_tasks():
    # if there are no tasks , print a message and return 
    if not tasks : print("No task to view ") ; return
    
    for index ,task in enumerate(tasks):
        status = "✔" if task["completed"] else "❌"    

        print(f'{index + 1 }.{task["task"]} {status} ')



if __name__ == "__main__":
    main()

