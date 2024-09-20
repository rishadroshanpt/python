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
        b_id=lib[-1]['id']+1
    b_name=input('Enter name of the book :')
    f=0
    for i in users:
        if i['b_name']==b_name:
            f=1
            print('Book already exists.')
            add_book()
    if f==0:
        b_price=int(input('Enter price of the book : '))
        b_stock=int(input('Enter number of books available : '))
        users.append({'b_id':b_id,'b_name':b_name,'b_price':b_price,'b_stock':b_stock})
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
                elif sub_ch==6:
                    break
        elif f==2:
            print('User login !')
            print('{:<5}{:<10}{:<15}{:<15}{:<10}{:<15}'.format('ID','NAME',"EMAIL",'USERNAME','PHONE','PASSWORD'))
            print('-'*70)
            print('{:<5}{:<10}{:<15}{:<15}{:<10}{:<15}'.format(user['id'],user['name'],user['email'],user['username'],user['phone'],user['password']))
    elif ch==3:
        break
    