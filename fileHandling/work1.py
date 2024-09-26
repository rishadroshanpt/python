# f=open('demo.txt','x')
# f.write('Hello')
# f.write('Python')
# f.write('World')
# f=open('demo.txt','r')
# a=f.readlines()
# l=len(a)
# f.seek(0)
# count=0
# for i in range(l):
#     b=f.readline().strip()
#     print(b[::-1])
#     c=len(b)
#     count=count+c
# print(count)

'''--------------to count numbers of letters---------------'''
# f=open('demo.txt','r')
# a=f.readlines()
# l=len(a)
# f.seek(0)
# count=0
# for i in range(l):
#     b=f.readline().strip()
#     print(b[::-1])
#     for i in b:
#         if i!=' ':
#             count+=1
# print(count)

'''
            dlrow olleH
            nohtyP
            dlroW
            21                          '''








'''------------------to count small and cap letters-------------------'''
# f=open('demo.txt','r')
# a=f.readlines()
# l=len(a)
# f.seek(0)
# count=0
# cap=0
# small=0
# for i in range(l):
#     b=f.readline().strip()
#     for i in b:
#         if i!=' ':
#             count+=1
#             if(i.isupper()):
#                 cap+=1
#             else:
#                 small+=1
# print('total letters :',count)
# print('total capital letters :',cap)
# print('total small letters :',small)

'''                 total letters : 21
                    total capital letters : 4
                    total small letters : 17                        '''









'''---------------to count number of words----------------'''
# f=open('demo.txt','r')
# a=f.readlines()
# f.seek(0)
# count=0
# for i in range(len(a)):
#     b=f.readline().strip()
#     c=b.split(' ')
#     for j in c:
#         if j!='':
#             count+=1
# print('total words :',count)

'''                 total words : 6                     '''














# f=open('demo.txt','w')
# f.write('welcome')
# f.write(' hello '+'world')
# f1=open('f1.txt','w')
# f1.write('ooooooooooooi')





f=open('f1.txt','w')
num=int(input('Enter a number : '))
for i in range(1,11):
    pro=i*num
    i=i
    num=num
    f.write(f'{i} x {num} = {pro} \n')

