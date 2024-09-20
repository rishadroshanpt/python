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
        users.append({'id':id,'name':name,'email':email,'username':username,'phone':phone,'password':password})
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
            while True:
                print('''
1.Add book
2.View Book
3.Update Book
4.Delete
5.View Users
6.Exit
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
        elif f==2:
            print('User login !')
            print('{:<5}{:<10}{:<15}{:<15}{:<10}'.format('ID','NAME',"EMAIL",'USERNAME','PHONE'))
            print('-'*70)
            print('{:<5}{:<10}{:<15}{:<15}{:<10}'.format(user['id'],user['name'],user['email'],user['username'],user['phone']))
    elif ch==3:
        break
    