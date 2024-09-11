def numbers():
    a=int(input('Enter ur first number : '))
    b=int(input('Enter ur second number : '))
    return a,b
def add():
    a,b=numbers()
    print(a+b)
def sub():
    a,b=numbers()
    print(a-b)
def mul():
    a,b=numbers()
    print(a*b)
def div():
    a,b=numbers()
    print(a/b)
def mod():
    a,b=numbers()
    print(a%b)
def floor():
    a,b=numbers()
    print(a//b)
def exp():
    a,b=numbers()
    print(a**b)
while True:
    print('''
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Modulus
6.Floor Division
7.Exponent
8.Exit''')
    ch=int(input('Enter your choice : '))
    if ch==1:
        add()
    elif ch==2:
        sub()
    elif ch==3:
        mul()
    elif ch==4:
        div()
    elif ch==5:
        mod()
    elif ch==6:
        floor()
    elif ch==7:
        exp()
    elif ch==8:
        break
    else:
        print('Invalid choice !')
