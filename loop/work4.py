
i=int(input("Enter starting number : "))
j=int(input("Enter ending number : "))
start=i
x=y=z=0

while i<=j:
    x=x+i
    if i%2==0:
        y=y+i
    else:
        z=z+i
    i+=1
print(f"sum of natural numbers between {start} and {j} is {x}")
print(f"sum of even numbers between {start} and {j} is {y}")
print(f"sum of odd numbers between {start} and {j} is {z}")