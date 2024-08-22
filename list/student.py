std=[]
while True:
    print('''
    1.Add student
    2.View
    3.Update    
    4.Delete
    5.Exit
    ''')
    ch=int(input('Enter your choice : '))
    if ch==1:
        name=input('Enter name :')
        age=int(input('Enter age : '))
        mark=int(input('Enter mark : '))
        std.append([name,age,mark])
    elif ch==2:
        print('{:<15}{:<10}{:<10}'.format('name','age','mark'))
        print('-'*35)
        for i in std:
            print('{:<15}{:<10}{:<10}'.format(i[0],i[1],i[2]))
    elif ch==3:
        name=input('Enter name of the student that you want to update : ')
        f=0
        for i in std:
            if name in i:
                new_mark=int(input('Enter new mark : '))
                i[2]=new_mark
                f=1
        if f==0:
            print('Student not in list.')
    elif ch==4:
        name=input('Enter name of the student that you want to delete : ')
        f=0
        for i in std:
            if name in i:
                std.remove(i)
                f=1
        if f==0:
            print('Student not in list.')
    elif ch==5:
        break
    else:
        print('Invalid choice !')
        
