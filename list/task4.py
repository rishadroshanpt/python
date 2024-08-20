l=[10,20,3,5.6,'abc']
x=0
for i in l:
    if type(i)==int or type(i)==float:
        x=x+i
print(f'sum of numbers in the list {l} is {x}')