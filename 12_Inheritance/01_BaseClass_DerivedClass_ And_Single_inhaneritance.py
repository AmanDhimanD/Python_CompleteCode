# Parent Class or Base Class
class School:
    school="M.G."

    def showDetails(self):
        print(f"This is student of {self.school}")
# Child Class or  Derived Class
class Students(School):
    studyAt="10"
    
    def Standard(self):
        print(f"Class :- {self.studyAt}")
    school="S.D."
    def showDetails(self):
        print(f"This is student of {self.school}")


nameSchool=School()
nameSchool.showDetails()
student=Students()
student.showDetails()