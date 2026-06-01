def add_task():
    print("\nEnter your task: ")
    b=input()
    task_list.append(b)
    print("\n")

def view_task():
    print("\nYour Tasks:")
    j=1
    for y in task_list:
        print(j,y)
        j=j+1
    print("\n")
    
def delete_task(i):
    if i<=len(task_list)-1:
        task_list.pop(i)
    else:
        print("Please enter a valid list index")
    print("\n")

task_list=[]
while True:
    print("1.Add a task\n2.View your task\n3.Delete task\n4.Exit")
    a=int(input("Enter your choice:"))
    if (a==1):
        add_task()
    elif(a==2):
        view_task()
    elif(a==3):
        i=int(input("\nEnter the index of task you want to delete:"))
        i=i-1
        delete_task(i)    
    elif(a==4):
        break
    else:
        print("Enter valid choice")
