to_do_list=[]

def options():
    print("What's on your mind? \n")
    print("1.View your current tasks \n")
    print("2.Add a task \n")
    print("3.Remove a task \n")
    print("4.Exit \n")

def show_list():
    if not to_do_list:
        print("You've got no upcoming tasks ")
    
    else:
        count=0
        for items in to_do_list:
            count+=1
            print(f'{count}:{items}')
    
    

def task_show():
    print("\nHere are all your tasks- ")
    show_list()

        

def task_add():
    task=input("\nEnter the task to be added ")
    to_do_list.append(task)

def task_delete():
        show_list()
        print("\n Which task you want to delete? ")
        td=input()
        td=int(td)
        to_do_list.pop(td-1)
        print("\nThe task is removed successfully! ")

while True:
    options()
    ans=input("Choose an Option! ")
    if ans == '1':
        if not to_do_list:
            print("\nYou have no upcoming tasks on your list! ")
        else:
            task_show()


                
    elif ans == '2':
        task_add()    

    elif ans == '3':
        if not to_do_list:
            print("\nYou have no upcoming tasks on your list! ")
        else:
            task_delete()
    
    elif ans == '4':
        break

    else:
        print("\nEnter a valid option\n")
        





    

