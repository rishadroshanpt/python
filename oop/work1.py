# class syn:
#     def python():
#         print('Python')
#     def php():
#         print('php')
#     def java():
#         print('Java')
# manu=syn
# manu.java()



class Bank:
    def __init__(self):
        self.name=input('Enter a name : ')
        self.age=int(input('Enter age : '))
        self.bal=0
    def deposit(self,amt):
        self.bal+=amt
        print('Deposite ',amt)
    def withdraw(self,amt):
        self.bal-=amt
        print('Withdraw ',amt)
    def balance(self):
        print('Balance ', self.bal)
obj=Bank()
obj.deposit(5000)
obj.balance()
obj.withdraw(1500)
obj.balance()

obj1=Bank()
obj1.deposit(3000)
obj1.balance()
obj1.withdraw(2500)
obj1.balance()