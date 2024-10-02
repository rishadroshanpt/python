
# INHERITANCE

#1 single inheritance

'''class syn:
    def python(self):
        self.a=10
        print('python',self.a)
    def php(self):
        print('php')
class novavi(syn):
    def DM(self):
        print('dm works')
    def web_dev(self):
        print('web dev')

novavi_staff=novavi()
novavi_staff.DM()
novavi_staff.python()
std1=syn()
std1.python()'''

#2 multiple inheritance

'''class father:
    def shop(self):
        print('shop')
    def car(self):
        print('car')
class mother:
    def dress_shop(self):
        print('dress shop')
class child(father,mother):
    def bike(self):
        print('bike')
somu=child()
somu.shop()
somu.car()
somu.dress_shop()
somu.bike()
'''

#work-school,tution(parent class) student(child class)

'''class school:
    def maths(self):
        print('maths')
    def physics(self):
        print('physics')
    def malayalam(self):
        print('malayalam')
class tution:
    def chemistry(self):
        print('chemistry')
    def physics_t(self):
        print('physics')
class student(school,tution):
    def sports(self):
        print('sports')
roshan=student()
roshan.maths
roshan.physics()
roshan.malayalam()
roshan.chemistry()
roshan.physics_t()
roshan.sports()'''

#3 multi-level inheritance

'''class kerala_university:
    def exam(self):
        print('exam')
    def result(self):
        print('result')
class college:
    def notes(self):
        print('notes')
    def labs(self):
        print('labs')
class student(kerala_university,college):
    def uniform(self):
        print('uniform')
sam=student()
sam.exam()
sam.result()
sam.notes()
sam.labs()
sam.uniform()
'''



#Heirarchichal inheritance

'''class Syn:
    def python(self):
        print('Python')
    def php(self):
        print('PHP')
class Nonteaching_staff(Syn):
    def admission(self):
        print('qqqqqq')
class Teaching_staff(Syn):
    def python1(self):
        print('Aswanth')
staff1=Nonteaching_staff()
staff1.admission()
staff1.python()
staff1.php()
staff2=Teaching_staff()
staff2.python1()'''






#hybrid inheritance
'''class Syn:
    def python(self):
        print('Python')
    def php(self):
        print('PHP')
class Nonteaching_staff(Syn):
    def admission(self):
        print('qqqqqq')
class Teaching_staff(Syn):
    def python1(self):
        print('Aswanth')
class student(Teaching_staff):
    def notes(self):
        print('Notes')
staff1=Nonteaching_staff()
staff1.admission()
staff1.python()
staff1.php()
staff2=Teaching_staff()
staff2.python1()
std=student()
std.notes()
std.python()
std.python1()
'''


class Animals():
    def animals(self):
        print('animals')
class Terrestrial(Animals):
    def terrestrial(self):
        print('Terrestrial')
class Aquatic(Animals):
    def fish(self):
        print('Fish')
class Shark(Aquatic):
    def shark(self):
        print('Shark')
class Lion(Terrestrial):
    def lion(self):
        print('Lion')
class Tiger(Terrestrial):
    def tiger(self):
        print('Tiger')
class Liger(Lion,Tiger):
    def Liger(self):
        print('Liger')
u1=Shark()
u1.shark()
u1.fish()
u1.animals()
u2=Liger()
u2.Liger()
u2.lion()
u2.tiger()
u2.animals()