from add import *
from sub import *
from div import *
from mul import *
from exp import *
from mod import *
from nums import *
while True:
    print('''
1.Add
2.Sub
3.Div
4.Mul
5.Exponent
6.Modulus
7.Exit
''')
    ch=int(input('Enter your choice : '))
    if ch==1:
        a,b=num()
        add(a,b)
    elif ch==2:
        a,b=num()
        sub(a,b)
    elif ch==3:
        a,b=num()
        div(a,b)
    elif ch==4:
        a,b=num()
        mul(a,b)
    elif ch==5:
        a,b=num()
        exp(a,b)
    elif ch==6:
        a,b=num()
        mod(a,b)
    elif ch==7:
        break
    else:
        print('Invalid choice !')