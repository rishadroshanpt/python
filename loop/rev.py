num=int(input('Enter a number : '))
number=num
i=1
x=0
rev=0
while num>0:
    x=num%10
    rev=(rev*10)+x
    num=num//10
print(f'Reverse of {number} is {rev}')