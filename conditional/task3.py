# a=int(input('1st number : '))
# b=int(input('2nd number : '))
# if a>b:
#     print('1st number is gretaer')
# elif a==b:
#     print('both numbers are equal')
# else:
#     print('2nd number is gretaer')




a=int(input('1st number : '))
b=int(input('2nd number : '))
c=int(input('3rd number : '))
if a>b:
    if a>c:
        print('1st number is largest')
    else:
        print('3rd number is largest')
else:
    if b>c:
        print('2st number is largest')
    else:
        print('3rd number is largest')
