employee=[]
while True:
    print(
        '''
1.Register Employee
2.Display Employees
3.Update Employee Deatils
4.Delete Employee
5.Add Task
6.Search Employee
7.Exit'''
    )
    ch=int(input('Enter your choice : '))
    if ch==1:
        id=int(input('Enter employee ID : '))
        name=input('Enter name of the employee : ')
        age=int(input('Enter age of the employee : '))
        place=input('Enter place of the employee : ')
        mobile=int(input('Enter mobile number : '))
        position=input('Enter position of the employee : ')
        salary=int(input('enter salary of the employee : '))
        employee.append([id,name,age,position,salary,mobile,place])
    elif ch==2:
        print('{:<10}{:<20}{:<5}{:<20}{:<10}{:<15}{:<20}'.format('ID','NAME','AGE','POSITION','SALARY','MOBILE','PLACE'))
        print('-'*100)
        for i in employee:
            print('{:<10}{:<20}{:<5}{:<20}{:<10}{:<15}{:<20}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    elif ch==3:
        id=int(input('Enter ID of the employee that you want to update : '))
        f=0
        for i in employee:
            if id in i:
                f=1
                while True:
                    print(
                    '''
1.Update Id
2.Update age
3.Update mobile
4.Update position
5.Update salary
6.Exit'''
                    )
                    ch=int(input('Enter your choice : '))
                    if ch==1:
                        new_id=int(input('Enter new employee ID : '))
                        i[0]=new_id
                    elif ch==2:
                        new_age=int(input('Enter age of the employee : '))
                        i[2]=new_age
                    elif ch==3:
                        new_mobile=int(input('Enter new mobile number : '))
                        i[5]=new_mobile
                    elif ch==4:
                        new_position=input('Enter new position : ')
                        i[3]=new_position
                    elif ch==5:
                        new_salary=int(input('Enter new salary : '))
                        i[4]=new_salary
                    elif ch==6:
                        break
                    else:
                        print('Invalid choice !')
        if f==0:
            print('Employee not found in list')
    elif ch==7:
        break
    else:
        print('Invalid Choice !')