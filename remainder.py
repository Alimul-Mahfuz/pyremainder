from datetime import datetime
from pickle import TRUE
COUNTENTITY=0
todolist=[]
class TODO:
    def __init__(self,name,address,datetime):
        self.todo={}
        self.todo['name']=name
        self.todo['address']=address
        #Phone is an set that's reference is recorded on details dictonary
        self.todo['time']=datetime   

def AddToDo():
    name=input("Enter Task Name: ")
    location=input("Enter location: ")
    my_string = str(input('Enter date(yyyy-mm-dd hh:mm): '))
    my_date = datetime.strptime(my_string, "%Y-%m-%d %H:%M")
    date=my_date
    myObj=TODO(name,location,date)
    todolist.append(myObj)
    global COUNTENTITY
    COUNTENTITY=COUNTENTITY+1
    # if(CheckConflict(date)==True):
    #     myObj=TODO(name,location,date)
    #     todolist.append(myObj)
    #     COUNTENTITY=COUNTENTITY+1
    # else:
    #     print("Task conflict: There already a task on this date and time")


def UpdateDetails(sl):
    global COUNTENTITY
    sl=sl-1
    if(int(sl) not in range(0,COUNTENTITY)):
        print("SL not exist")
        pass
    else:
        print("1. Update task name: ")
        print("2. Update Address: ")
        print("3. Update datetime: ")
        print("4. q to exit ")
        exit=input("Enter choice: ")
        if(exit=='q'):
            pass
        elif(int(exit)==1):
            todolist[sl].todo['name']=input("Enter new Name: ")
            pass
        elif(int(exit)==2):
            todolist[sl].todo['address']=input("Enter new Address: ")
            pass
        elif(int(exit)==3):
            my_string = str(input('Enter new date(yyyy-mm-dd hh:mm): '))
            my_date = datetime.strptime(my_string, "%Y-%m-%d %H:%M")
            date=my_date
            todolist[sl].todo['time']=date
    
def PrintDetails():
    for i in range(len(todolist)):
        print('\n')
        print('#SL{}----------------------'.format(i+1))
        print("ToDo Name: {}".format(todolist[i].todo['name']))
        print("Address: {}".format(todolist[i].todo['address']))
        print("Time: {}".format(todolist[i].todo['time']))

def SearchTask():
    found=False
    index=0
    name=input("Enter task name to search: ")
    for x in todolist:
        index=index+1
        if x.todo['name']==name:
            print("task found")
            found=True
            print("Details of the task")
            print("Name: {}".format(x.todo['name']))
            print("Address: {}".format(x.todo['address']))
            print("Time: {}".format(x.todo['time']))
            ch=input("Want to update the task y/n: ")
            if(ch=='y' or ch=='Y'):
                UpdateDetails(index)
            if(ch=='n' or ch=='N'):
                print('Okay Thanks you')
            pass
    if(found==False):
        print("task doesn't exists")

def CheckConflict(time):
    for i in range(len(todolist)):
        if(todolist[i].todo['time']==time):
            return True
        else:
            return False

def DeleteTask():
    sl=int(input("Enter the sl to delete: "))
    sl=sl-1
    if(int(sl) not in range(0,COUNTENTITY)):
        print("SL not exist")
        pass
    del(todolist[sl])
    print("Task Deleted Successfully")

def viewUpcommingTask(dt_string):
    for x in todolist:
        if(x.todo['time']>dt_string):
            print("ToDo Name: {}".format(x.todo['name']))
            print("Address: {}".format(x.todo['address']))
            print("Time: {}".format(x.todo['time']))
        else:
            print('No task remaining')




def Print():
    fname="./pythonProject/ReminderApp/data.txt"
    with open(fname,'w') as file_obj:
        for i in range(len(todolist)):
            file_obj.writelines('\n')
            file_obj.writelines('\n#SL{}----------------------'.format(i+1))
            file_obj.writelines("\nToDo Name: {}".format(todolist[i].todo['name']))
            file_obj.writelines("\nAddress: {}".format(todolist[i].todo['address']))
            file_obj.writelines("\nTime: {}".format(todolist[i].todo['time']))

def PrintPromt():
    print('\n')
    print("==============WELCOME TO PYREMINDER==============")
    print("1. Add a new ToDo")
    print("2. View ToDo List")
    print("3. Update exixting ToDo list")
    print("4. View Upcomming task")
    print("5. Search")
    print("6. Delete")
    print("7. Print your ToDo List")
    a=input("Enter your choice or press q to exit:  ")
    return a
a=PrintPromt()

while(a!='q'):
    if int(a)==1:
        AddToDo()
        a=PrintPromt()
    if int(a)==2:
        if(len(todolist)==0):
            print("Task List is empty")
        else:
            PrintDetails()       
        a=PrintPromt()
    if int(a)==3:
        sl=int(input("Enter SL of the task: "))
        UpdateDetails(sl)
        a=PrintPromt()
    if int(a)==4:
        now = datetime.now()
        dt_string = now.strptime("%Y-%m-%d %H:%M")
        viewUpcommingTask(dt_string)
        a=PrintPromt()
    if int(a)==5:
        SearchTask()
        a=PrintPromt()
    if int(a)==6:
        DeleteTask()
        a=PrintPromt()
    if int(a)==7:
        Print()
        a=PrintPromt()
        
    




