# for i in range(1,4):
#     for j in range(i):
#         print(j,end="  ")
#     print()

'''
0  
0  1  
0  1  2  
'''

# a=0
# for i in range(1,4):
#     for j in range(i):
#         print(a,end="  ")
#         a+=1
#     print()

'''
0  
1  2
3  4  5
'''

# a=0
# for i in range(1,4):
#     for j in range(i):
#         print(a,end="  ")
#     print()
#     a+=1

'''
0  
1  1
2  2  2
'''
a=0
for i in range(1,4):
    for j in range(i):
        print(a-j,end="  ")
    a+=1
    print()

'''
0  
1  0
2  1  0
'''