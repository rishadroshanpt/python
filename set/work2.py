'''------------------------unique items in more than one set--------------------'''

php={'a','b','c','h'}
java={'a','b','h','t'}
python={'c','d','e'}
s1=php.difference(java).difference(python)
s2=java.difference(php).difference(python)
s3=python.difference(java).difference(php)
u=s1.union(s2).union(s3)
print(u)

'''             {'d', 'e', 't'}             '''