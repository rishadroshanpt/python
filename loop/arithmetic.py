while True:
    print('''
1-Addition
2-Subtraction
3-Multiplication
4-Division
5-Floor Division
6-Modulus
7-Exponent
8-Exit''')
    ch=int(input('Enter your choice : '))
    if ch<8 and ch>0:
        a=int(input('Enter 1st number : '))
        b=int(input('Enter 2nd number : '))
    if ch==1:
        print(f'Sum of {a} and {b} is {a+b}')
    elif ch==2:
        print(f'Minuend of {a} and {b} is {a-b}')
    elif ch==3:
        print(f'Product of {a} and {b} is {a*b}')
    elif ch==4:
        print(f'Quotient of {a} and {b} is {a/b}')
    elif ch==5:
        print(f'Quotient of {a} and {b} without decimal value is {a//b}')
    elif ch==6:
        print(f'Modulus of {a} and {b} is {a%b}')
    elif ch==7:
        print(f'Exponent of {a} and {b} is {a**b}')
    elif ch==8:
        break
    else:
        print('Invalid Choice.')