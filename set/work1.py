# s={1,3,5,7.8,3,'abc',7.8}
# for i in s:
#     print(i)





'''------------------to delete duplicate values in a list using set ------------------'''

# l=[1,2,4,3,6,5,2,3,1]
# s=set(l)
# l=list(s)
# print(l)

'''         [1, 2, 3, 4, 5, 6]          '''






'''------------------methods in set------------------'''

# s={1,2,3,4,2,3,1,5}
# print(s)
# s.pop()
# print(s)
# s.add(15)
# print(s)
# s.discard(100)
# print(s)
# s.remove(4)
# print(s)
# s.clear()
# print(s)

'''             {1, 2, 3, 4, 5}
                {2, 3, 4, 5}
                {2, 3, 4, 5, 15}
                {2, 3, 4, 5, 15}
                {2, 3, 5, 15}
                set()                           '''



s={1,2,3,4,5}
s1={1,3,4}
# print(s.difference(s1))
'''                 {2, 4, 5}               '''
# print(s.union(s1))
'''                 {1, 2, 3, 4, 5}           '''
# print(s1.issubset(s))
'''                 True                     '''
# print(s.issuperset(s1))
'''                 True                     '''
# print(s.symmetric_difference(s1))
'''                 {2, 5}                  '''
s.update({11,12,13})
print(s)

