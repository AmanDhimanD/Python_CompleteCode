class StudentInfo:
    formType="Student Detalis"
    def printData(self):
        print(f"Name is {self.name}.")
        print(f"Roll Number is {self.number}.")


nameOfApplication=StudentInfo()
nameOfApplication.name="Aman"
nameOfApplication.number="1030"
nameOfApplication.printData()