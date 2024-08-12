salary=int(input('Enter your current salary : '))
service=int(input('Enter your year of service : '))
x=salary
if service>=5:
    bonus=x/100*5
    salary+=bonus
print('Your salary is ',salary)
