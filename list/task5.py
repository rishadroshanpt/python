l=[1,2,4,3,5,45,34,6]
print(l)
L=[]
L2=[]
for i in l:
    if i%2==0:
        L.append(i)
print(f'Numbers that are divisible by 2 in the list {l} is {L}')
for i in L:
    i=i**2
    L2.append(i)
print(f'Square of the items in the list {L} is {L2}')
