def register():
    print('Registration Page')
    if len(users)==0:
        id=101
    else:
        id=users[-1]['id']+1
    email=input('enter your email :')
    f=0
    for i in users:
        if i['email']==email:
            f=1
            print('User already exists.')
            register()
    if f==0:
        name=str(input('enter your name : '))
        username=email
        phone=int(input('enter your number : '))
        password=input('enter the password : ')
        book=[]
        users.append({'id':id,'name':name,'email':email,'username':username,'phone':phone,'password':password,'books':book})
def login():
    uname=input('Enter Username : ')
    passwd=input('Enter password : ')
    f=0
    if uname=='admin' and passwd=='admin':
        f=1
    user=''
    for i in users:
        if i['username']==uname and i['password']==passwd:
            f=2
            user=i
    return f,user
def add_book():
    if len(lib)==0:
        b_id=1001
    else:
        b_id=lib[-1]['b_id']+1
    b_name=input('Enter name of the book :')
    f=0
    for i in lib:
        if i['b_name']==b_name:
            f=1
            print('Book already exists.')
            add_book()
    if f==0:
        b_price=int(input('Enter price of the book : '))
        b_stock=int(input('Enter number of books available : '))
        lib.append({'b_id':b_id,'b_name':b_name,'b_price':b_price,'b_stock':b_stock})
def view_book():
    print('{:<10}{:<10}{:<10}{:<10}'.format('ID','NAME','PRICE','QTY'))
    print('-'*40)
    for i in lib:
        print('{:<10}{:<10}{:<10}{:<10}'.format(i['b_id'],i['b_name'],i['b_price'],i['b_stock']))
def update_book():
    b_id=int(input('Enter the id of the book that you want to update : '))
    f=0
    for i in lib:
        if b_id==i['b_id']:
            f=1
            while True:
                print('''
1.Update price.
2.Update Qty
3.Exit.
''')
                ch=int(input('Enter your choice : '))
                if ch==1:
                    new_price=int(input('Enter the new price of the book : '))
                    i['b_price']=new_price
                elif ch==2:
                    new_qty=int(input('Enter the new qty of the book : '))
                    i['b_stock']=new_qty
                elif ch==3:
                    break
                else:
                    print('Invalid choice !')
    if f==0:
        print('ID not found .')
def delete_book():
    b_id=int(input('Enter the id of the book that you want to delete : '))
    f=0
    for i in lib:
        if b_id==i['b_id']:
            f=1
            lib.remove(i)
    if f==0:
        print('ID not found .')
def view_users():
    print('{:<5}{:<10}{:<15}{:<15}{:<10}'.format('ID','NAME',"EMAIL",'USERNAME','PHONE'))
    print('-'*55)
    for i in users:
        print('{:<5}{:<10}{:<15}{:<15}{:<10}'.format(i['id'],i['name'],i['email'],i['username'],i['phone']))
def update_profile():
    while True:
        print('''
1.Update email
2.Update username
3.Update phone number
4.Exit
''')
        ch=int(input('Enter your choice : '))
        if ch==1:
            new_email=input('Enter your new email : ')
            user['email']=new_email
        elif ch==2:
            new_username=input('Enter your new username : ')
            user['username']=new_username
        elif ch==3:
            new_phone=int(input('Enter new phone number : '))
            user['phone']=new_phone
        elif ch==4:
            break
        else:
            print('Invalid choice !')
def rent_a_book(user):
    view_book()
    id=int(input('Enter the id of the book that you want to rent : '))
    f=0
    for i in lib:
        if i['b_id']==id:
            f=1
            user['books'].append(id)
            i['b_stock']-=1
            print('Book rented successfully .')
    if f==0:
        print('Invalid choice!')
def return_book(user):
    book_in_hand(user)
    id=int(input('Enter the id of the book that you want to return : '))
    f=0
    for i in lib:
        if i['b_id']==id and id in user['books']:
            f=1
            user['books'].remove(id)
            i['b_stock']+=1
            print('Book returned successfully .')
    if f==0:
        print('Invalid choice!')
def book_in_hand(user):
    print(user['books'])
def view_user(user):
    print('ID :',user['id'])
    print('NAME :',user['name'])
    print('EMAIL :',user['email'])
    print('USERNAME :',user['username'])
    print('PHONE :',user['phone'])
    print('BOOKS :',user['books'])
users=[]
lib=[]
while True:
    print('''
    1.Register as User
    2.Login
    3.EXIT''')
    ch=int(input('enter your choice : '))
    if ch==1:
        register()
    elif ch==2:
        f,user=login()
        if f==0:
            print('Incorrect password or username !')
        elif f==1:
            print('Admin login !')
            while True:
                print('''
1.Add book
2.View Book
3.Update Book
4.Delete
5.View Users
6.Logout
''')
                sub_ch=int(input('Enter your choice : '))
                if sub_ch==1:
                    add_book()
                elif sub_ch==2:
                    view_book()
                elif sub_ch==3:
                    update_book()
                elif sub_ch==4:
                    delete_book()
                elif sub_ch==5:
                    view_users()
                elif sub_ch==6:
                    break
                else:
                    print('Invalid choice !')
        elif f==2:
            print('User login !')
            while True:
                print('''
1.View Book
2.View User
3.Update profile
4.Lent/Rent
5.Return book
6.Book in hand
7.Logout
''')
                ch=int(input('Enter your choice : '))
                if ch==1:
                    view_book()
                elif ch==2:
                    view_user(user)
                elif ch==3:
                    update_profile()
                elif ch==4:
                    rent_a_book(user)
                elif ch==5:
                    return_book(user)
                elif ch==6:
                    book_in_hand(user)
                elif ch==7:
                    break
                else:
                    print('Invalid choice !')
    elif ch==3:
        break
    else:
        print('Invalid choice !')