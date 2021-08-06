class Freeelancer:
    company="Fivver"
    level= 0

    def upgradeLevel(self):
        self.level= self.level+1

class Emplyoee:
    company="upGrad"
    e_code=101


# class Programmer(Freeelancer,Emplyoee): 
# print first Freeelancer=fivver
class Programmer(Emplyoee,Freeelancer,:
    name="Rayne"
# print first Emplyoee ="upGrad"


p=Programmer()
p.upgradeLevel()
print(p.company)