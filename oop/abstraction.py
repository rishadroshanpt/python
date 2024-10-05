from abc import ABC,abstractmethod
class syn(abc):
    def reg(self):
        print('reg')
class std(syn):
    def reg(self):
        name=input('Enter your name : ')
class staff(syn):
    def reg(self):
        print('reg')