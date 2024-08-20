'''         largest         '''

# l=[1,50,3,6,4,2,10,4]
# print(l)
# largest=l[0]
# for i in l:
#     if i>largest:
#         largest=i
# print(largest)


'''         smallest            '''

# l=[1,50,3,6,4,2,10,0,4]
# print(l)
# smallest=l[0]
# for i in l:
#     if i<smallest:
#         smallest=i
# print(smallest)


'''         reverse of contents         '''

# l=['apple','orange','mango']
# for i in l:
#     print(i[::-1])

'''------------------------------------------------------------------'''

l=['apple','orange','mango']
rev=''
for i in l:
    for j in i:
        rev=j+rev
print(rev)