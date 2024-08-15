number=i=int(input('Enter starting point :'))
j=int(input('Enter ending point :'))
x=0
for i in range(i,j+1):
    if i%2!=0:
        x=x+i
        print(i)
print(f'Sum of odd numbers from {number} to {j} is {x}')