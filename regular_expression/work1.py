# import re
# a='abcd789'
# print(re.search('[a-z].*[0-9]',a))



# number validation
'''import re
no=input('Enter your mobile no. : ')
if len(no)==10 and re.search('[6-9].{9}',no) and no.isdigit :
    print('Valid ')
else:
    print('Invalid number')'''



# email validation
'''import re
mail=input('Enter your email : ')
if re.search('^[a-z].*@gmail.com$',mail) :
    print('valid')
else:
    print('Invalid')'''




#password validation
import re
pw=input('Enter your password : ')
if len(pw)>=8 and len(pw)<=12 and re.search('^[A-z0-9].*[@#$%0-9]',pw) and not(pw.isdigit()) :
    print('valid')
else:
    print('Invalid')