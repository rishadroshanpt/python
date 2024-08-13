unit=int(input('Enter number of units : '))
if unit<=100:
    print('No charge')
elif unit>100 and unit<=200:
    charge=(unit-100)*5
    print('Total chrage is ',charge)
else:
    charge=(unit-200)*10
    print('Total chrage is ',charge+500)

