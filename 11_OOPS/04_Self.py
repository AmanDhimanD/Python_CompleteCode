class Employee:
    company="Facebook"
    def getSalary(self):
        print(f"Salary for this employee Working in {self.company} is {self.salary}.")


rayne=Employee()
rayne.salary=100000
rayne.getSalary() #Employee.getSalary(harry)
