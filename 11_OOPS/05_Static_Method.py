class Employee:
    company="Facebook"
    def getSalary(self):
        print(f"Salary for this employee Working in {self.company} is {self.salary}.")

    #Decorator :-> there are no need of self parameter  
    @staticmethod
    def greet():
        print("Thanks !!!!")

rayne=Employee()
rayne.salary=100000
rayne.getSalary() #Employee.getSalary(harry)
rayne.greet()
