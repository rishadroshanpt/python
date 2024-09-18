emp=[]
def login():
    uname=input('Enter username : ')
    passwd=input('Enter password : ')
    f=0
    if uname=='admin' and passwd=='admin':
        f=1
    return f
def add_emp():
    id=int(input('Enter id : '))
    f=0
    for i in emp:
        if i['id']==id:
            f=1
            print('Id already exists !')
            add_emp()
    if f==0:
        name=input('Enter employee name : ')
        dob=input('Enter date of birth : ')
        salary=int(input('Enter salary : '))
        position=input('Enter position : ')
        emp.append({'id':id,'name':name,'dob':dob,'salary':salary,'position':position})
def display_emp():
    print('{:<5}{:<10}{:<10}{:<10}{:<10}'.format('ID','NAME','DOB','SALARY','POSITION'))
    print('-'*45)
    for i in emp:
        print('{:<5}{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['dob'],i['salary'],i['position']))
def update_emp():
    id=int(input('Enter id : '))
    f=0
    for i in emp:
        if i['id']==id:
            f=1
            new_salary=int(input('Enter updated salary : '))
            new_position=input('Enter new position : ')
            i['salary']=new_salary
            i['position']=new_position
    if f==0:    
        print('Id does not exists !')
def delete_emp():
    id=int(input('Enter id : '))
    f=0
    for i in emp:
        if i['id']==id:
            f=1
            emp.remove(i)
    if f==0:    
        print('Id does not exists !')
while True:
    print('''
1.Login
2.Exit''')
    ch=int(input('Enyter your choice : '))
    if ch==1:
        f=login()
        if f==1:
            while True:
                print('''
1.Add employee ID
2.Display
3.Update
4.Delete
5.Logout''')
                sub_ch=int(input('Enter your choice : '))
                if sub_ch==1:
                    add_emp()
                elif sub_ch==2:
                    display_emp()
                elif sub_ch==3:
                    update_emp()
                elif sub_ch==4:
                    delete_emp()
                elif sub_ch==5:
                    break
                else:
                    print('Invalid choice !')
        elif f==0:
            print('incorrect password or username !')
    elif ch==2:
        break
    else:
        print('Invalid Choice !')

        