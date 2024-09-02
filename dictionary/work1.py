# d={'name':'appu','age':21,'place':'ekm'}
# print('name ',d['name'])
# print('place ',d['place'])
# print('age ',d['age'])

'''         name  appu
            place  ekm
            age  21         '''







# d={'name':'appu','age':21,'place':'ekm'}
# for i in d:
#     print(i)

'''         name
            age
            place           '''








# d={'name':'appu','age':21,'place':'ekm'}
# for i in d:
#     print(d[i])

'''         appu
            21
            ekm         '''






# d={'name':'appu','age':21,'place':'ekm'}
# for i in d:
#     print(i,d[i])

'''         name appu
            age 21
            place ekm           '''


# d={'name':'appu','age':21,'place':'ekm'}
# d['name']='dom'
# d['mark']=47
# print(d)
# for i in d:
#     print(i,d[i])

'''         {'name': 'dom', 'age': 21, 'place': 'ekm', 'mark': 47}
            name dom
            age 21
            place ekm
            mark 47             '''



# d={'name':'appu','age':21,'place':'ekm'}
# if d['age']==21:
#     print('Available')
# else:
#     print('Not available')

'''         Available           '''








# d={'name':'appu','age':21,'place':'ekm'}
# print(d.get('name'))
'''         appu            '''
# print(d.items())
'''         dict_items([('name', 'appu'), ('age', 21), ('place', 'ekm')])           '''
# print(d.keys())
'''         dict_keys(['name', 'age', 'place'])         '''
# print(d.values())
'''         dict_values(['appu', 21, 'ekm'])            '''
# d.pop('name')
# print(d)
'''         {'age': 21, 'place': 'ekm'}         '''
# d.popitem()
# print(d)
'''         {'name': 'appu', 'age': 21}         '''
# a=d.copy()
# print(id(a))
# print(id(d))
# d['mark']=29
# print(d)
# print(a)
'''         {'name': 'appu', 'age': 21, 'place': 'ekm', 'mark': 29}
            {'name': 'appu', 'age': 21, 'place': 'ekm'}         '''
# l=[1,2,3]
# print(d.fromkeys(l))
'''         {1: None, 2: None, 3: None}         '''
# d.setdefault('mark')
# print(d)
'''         {'name': 'appu', 'age': 21, 'place': 'ekm', 'mark': None}           '''








d={}
name=input('Enter name : ')
age=int(input('Enter age : '))
place=input('Enter place : ')
d['name']=name
d['age']=age
d['place']=place
print(d)

'''         Enter name : anu
            Enter age : 21
            Enter place : mlp
            {'name': 'anu', 'age': 21, 'place': 'mlp'}          '''