l=['apple','welcome','orange','grape']
largest=len(l[0])
for i in l:
    if len(i)>largest:
        largest=len(i)
        large=i
print('largest item in the list is ',large)