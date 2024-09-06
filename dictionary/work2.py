'''         to print the word of a single digit number           '''

# a={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# b=int(input('Enter a number : '))
# print(a[b])

'''         Enter a number : 5
            five            '''



'''         to print the word of numbers           '''

# a={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# num=int(input('Enter a number : '))
# s=''
# while num>0:
#     d=num%10
#     s=a[d]+' '+s
#     num//=10
# print(s)

'''         Enter a number : 567542
            five six seven five four two            '''











'''         to access a list in a dict whic is in list          '''

# a=[{'name':'anu','age':21,'project':['ems','sms']}]
# print(a[0]['project'][0])

'''         ems         '''










a=[{'name':'anu','age':21,'project':['ems','sms']}]
b=input('enter a project name : ')
a[0]['project'].append(b)
print(a)
b=input('enter a project name : ')
a[0]['project'].remove(b)
print(a)

'''         enter a project name : eee
            [{'name': 'anu', 'age': 21, 'project': ['ems', 'sms', 'eee']}]
            enter a project name : ems
            [{'name': 'anu', 'age': 21, 'project': ['sms', 'eee']}]         '''