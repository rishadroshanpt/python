price=int(input('Enter the coats of your bike : '))
if price>100000:
    tax=price/100*15
elif price>50000 and price<=100000:
    tax=price/100*10
else:
    tax=price/100*5
print('Total tax to be paid : ',tax)