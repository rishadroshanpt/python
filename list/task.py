l=[1,2,1,5,8,'abc',8,'abc']
print(l)
L=[]
for i in l:
        if i not in L:
            L.append(i)
print(L)