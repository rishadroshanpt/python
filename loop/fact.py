num=int(input('Enter a number : '))
number=num
i=1
fact=1
while num>i:
    fact=fact*num
    num-=1
print(f"factorial of {number} is {fact}")