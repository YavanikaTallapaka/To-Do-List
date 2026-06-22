def add_task():
    task=input("\nEnter your task: ")
    f=open("Dataset.txt","a")
    f.write(task+"\n")
    print("Done!!!")
    f.close()
         
def view_task():
    print("\nYour Tasks:")
    f1=open("Dataset.txt","r")
    lines=f1.readlines()
    i=1
    if(len(lines)==0):
        print("No Tasks given yet")
        f1.close()
        return
    for data in lines:
        print(f"{i}. {data.strip()}")#strip removes extra spaces and newlines
        i=i+1
    print("\n")
    f1.close()   

    
def delete_task(i):
    f2=open("Dataset.txt","r")
    task=f2.readlines()
    f2.close()
    if i>=0 and i<len(task):
        task.pop(i)
    else:
        print("Please enter a valid list index")
    print("\n")
    f3=open("Dataset.txt","w")
    f3.writelines(task)
    f3.close()
    
while True:
    print("1.Add a task\n2.View your task\n3.Delete task\n4.Exit")
    a=int(input("Enter your choice:"))
    if (a==1):
        add_task()
    elif(a==2):
        view_task()
    elif(a == 3):
        f4 = open("Dataset.txt", "r")
        check = f4.readlines()
        f4.close()

        if(len(check) == 0):
            print("Empty List, can't delete data\n")
            continue
        i=int(input("\nEnter the index of task you want to delete:"))
        i=i-1  
        delete_task(i)    
    elif(a==4):
        break
    else:
        print("Enter valid choice")
