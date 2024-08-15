num=int(input('Enter a number : '))
number=num
sum=x=0
for i in range(num):
    x=num%10
    sum=sum+x
    num=num//10
print(f'Sum of digits of {number} is {sum}')