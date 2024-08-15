number=i=int(input('Enter starting point :'))
j=int(input('Enter ending point :'))
x=0
for i in range(i,j+1):
    x=x+i
    print(i)
print(f'Sum of numbers from {number} to {j} is {x}')