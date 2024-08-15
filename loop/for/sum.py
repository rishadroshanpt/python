number=i=int(input('Enter starting point :'))
j=int(input('Enter ending point :'))
x=z=y=0
for i in range(i,j+1):
    x=x+i
    if i%2==0:
        y=y+i
    else:
        z=z+i
print(f'Sum of numbers from {number} to {j} is {x}')
print(f'Sum of even numbers from {number} to {j} is {y}')
print(f'Sum of odd numbers from {number} to {j} is {z}')