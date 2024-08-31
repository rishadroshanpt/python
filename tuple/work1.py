# a=(10,20,25)
# print(a)

'''         (10, 20, 25)            '''



# a=10,20,25
# print(a)

'''         (10, 20, 25)            '''





# a=10,20,25,30,45
# print(a.index(20))

'''         1           '''




# a=10,20,25,30,45,25
# print(a.count(25))

'''     2       '''




# a=10,20,25,30,45,25
# for i in a:
#     print(i)

'''         10
            20
            25
            30
            45
            25          '''




# a=10,20,25,30,45,25
# i=int(input('Enter value to find : '))
# if i in a:
#     print('Yes')
# else:
#     print('No')


# t=(10,[1,2],11)
# print(t)
# t[1].append(3)
# print(t)

'''         (10, [1, 2], 11)
            (10, [1, 2, 3], 11)                  '''







# t=(10,11,12,13)
# print(t)
# l=list(t)
# l.pop()
# l[-1]=111
# t=tuple(l)
# print(t)

'''         (10, 11, 12, 13)
            (10, 11, 111)               '''









t=(1,2,3,4,3,5,2,1,3,2)
a=int(input('Enter a value : '))
c=t.count(a)
print('count : ',c)
pos=0
while c>0:
    p=t.index(a,pos)
    pos=p+1
    print(p)
    c-=1

'''         Enter a value : 2
            count :  3
            1
            6
            9                       '''