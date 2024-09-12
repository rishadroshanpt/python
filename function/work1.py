# def sample():
#     print('Welcome........')
#     a=46
#     print(a)
# sample()
# b=[1,2,3,4,5]
# print(b)
# b.append(10)
# sample()
# print(b)
# b.append(10)
# sample()
# print(b)








# def sample():
#     a=10
#     print('Inside fun a=',a)
# a=20
# sample()
# print('outside fun a=',a)
















# def sample():
#     a=20
#     b=12
#     return 'wlecome',a,b
# w,a,b=sample()
# print(w)
# print(a)
# print(b)

'''                 wlecome
                    20
                    12                  '''












#------------------------positional argument--------------------

# def sample(a,b):
#     print(a,b)
# sample(10,20)
# sample(['qq',1,2,40],3)

'''                 10 20
                    ['qq', 1, 2, 40] 3                  '''


























#------------------------keyword argument--------------------

# def sample(name,age):
#     print('Name : ',name)
#     print('Age : ',age)
# sample(age=20,name='anu')

'''                 Name :  anu
                    Age :  20               '''
























# def sample(name='appu',age=20):
#     print(name,age)
# sample('anu')
# sample('manu',22)
# sample(age=25)
# sample()

'''                 anu 20
                    manu 22
                    appu 25
                    appu 20                 '''


















# def sample(*a):
#     print(a)
# sample(23)
# sample('hoora')
# sample('welcome','hello',12)

'''             (23,)
                ('hoora',)
                ('welcome', 'hello', 12)                '''






















def sample(**a):
    print(a)
sample()
sample(name='appu',age=15)