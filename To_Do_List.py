#Function definitions
Tasks=[]
#To add task
def AddTask():
    n=int(input("Enter number of tasks to add:"))
    for i in range(n):
        t=input("Enter task:")
        Tasks.append("[ ] "+t)

# To remove task
def Remove():
  if len(Tasks)>0:
    for i in range(len(Tasks)):
        print(i+1,". ",Tasks[i])
    n=int(input("Enter task number to remove:"))
    if 0 < n <= len(Tasks):
       Tasks.pop(n-1)
       print("\nThe task is removed succesfully!!\n")
    else:
        print("\ninvalid task number\n")
  else:
      print("\nNo tasks available\n")

# To Mark it as done
def Markdone():
  if len(Tasks)>0:
    for i in range(len(Tasks)):
        print(i+1,". ",Tasks[i])
    n=int(input("Enter task number to mark as done:"))
    if 0 < n <= len(Tasks):
       Tasks[n-1]=Tasks[n-1].replace("[ ] ","[x] ")
       print("\nThe task is mark as done\n")
    else:
        print("\ninvalid task number\n")
  else:
      print("\nNo tasks available\n")
    
#To View
def View():
    if len(Tasks)>0:
        for task in Tasks:
            print(task)
    else:
         print("\nNo tasks available\n")


#To_D0 list
try:
    f = open("TO_DO_LIST.txt", "r")
    for line in f:
        Tasks.append(line.strip())
    f.close()
except FileNotFoundError:
    pass
while True:
    print("="*60)
    print("\n OPERATIONS AVAILABLE \n")
    print(""" 1. Add task
    2. Remove task
    3. Mark as done
    4. View Task
    5. Quit\n""")
    print("="*60,"\n")
    ch=int(input("Enter the choice:"))
    if ch not in (1,2,3,4,5):
        print("\ninvalid choice\n")
    elif ch==1:
        AddTask()
        f = open("TO_DO_LIST.txt", "w")
        for task in Tasks:
              f.write(task + "\n")
        f.close()
    elif ch==2:
        Remove()
        f = open("TO_DO_LIST.txt", "w")
        for task in Tasks:
              f.write(task + "\n")
        f.close()
    elif ch==3:
        Markdone()
        f = open("TO_DO_LIST.txt", "w")
        for task in Tasks:
              f.write(task + "\n")
        f.close()
    elif ch==4:
        View()
    elif ch==5:
        break
    
