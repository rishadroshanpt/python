# i=int(input("Enter starting number : "))
# j=int(input("Enter ending number : "))
# while i<=j:
#     if i%2==1:
#         print(i)
#     i+=1







i=int(input("Enter starting number : "))
j=int(input("Enter ending number : "))
start=i
x=0
while i<=j:
    if i%2==1:
        x=x+i
    i+=1
print(f"sum of odd numbers between {start} and {j} is {x}")