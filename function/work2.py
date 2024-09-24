# data=lambda a,b:a+b
# print(data(10,15))

'''         25          '''



# data=lambda:print('Welcome')
# data()

'''         Welcome         '''


# data=lambda:('Welcome')
# print(data())

'''         Welcome         '''


'''             filter using lambda function             '''
# l=[1,2,3,4,5,6]
# print(list(filter(lambda x:x%2==0,l)))

'''             [2, 4, 6]                   '''




'''             filter using normal function             '''
# l=[1,2,3,4,5,6]
# def num(x):
#     return x%2==0
# print(list(filter(num,l)))

'''             [2, 4, 6]                    '''





'''             string using filter in lambda               '''
# l=['hello','welcome','kooi','kid','happy']
# print(list(filter(lambda x:'o' in x,l)))

'''             ['hello', 'welcome', 'kooi']                '''







'''             string using filter in lambda               '''
# l=['hello','welcome','kooi','kid','happy']
# def string(x):
#     return 'o' in x
# print(list(filter(string,l)))

'''             ['hello', 'welcome', 'kooi']                '''




'''             map using lambda function                     '''
# l=[1,2,3,4,5]
# print(list(map(lambda x:x**2,l)))

'''             [1, 4, 9, 16, 25]               '''






'''             map using normal function                     '''
l=[1,2,3,4,5]
def num(x):
    return x+10
print(list(map(num,l)))

'''             [11, 12, 13, 14, 15]               '''