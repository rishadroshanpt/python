'''class school:
    def notes(self):
        print('notes in school')
class std(school):
    def notes(self):
        print('notes in std')
    
manu=std()
manu.notes()'''

#                       notes in std










#                       using init constrain
'''class bank:
    def __init__(self):
        print('bank details')
class user(bank):
    def __init__(self):
        print('user details')
sbi=bank()
manu=user()'''

                        # bank details
                        # user details









                            #using super function
'''class school:
    def notes(self):
        print('notes in school')
class ed(school):
    def notes(self):
        super().notes()
        print('notes in ed')
class std(ed):
    def notes(self):
        super().notes()
        print('notes in std')
    
manu=std()
manu.notes()'''

                            # notes in school
                            # notes in ed
                            # notes in std







                            # using super function in __init__
'''class bank:
    def __init__(self):
        print('bank details')
class user(bank):
    def __init__(self):
        super().__init__()
        print('user details')
manu=user()'''

                            # bank details
                            # user details







                        # transfering of data

class school:
    def notes(self,sub):
        print('notes in school',sub)
class std(school):
    def notes(self,sub):
        super().notes(sub)
        print('notes in std')
    
manu=std()
manu.notes('py')

                        # notes in school py
                        # notes in std
