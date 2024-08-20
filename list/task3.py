l=[1,2,3,4,5]
x=0
y=0
for i in l:
    if i%2==0:
        x=x+i
    else:
        y=y+i
print(f'sum of even numbers in the list {l} is {x}')
print(f'sum of odd numbers in the list {l} is {y}')