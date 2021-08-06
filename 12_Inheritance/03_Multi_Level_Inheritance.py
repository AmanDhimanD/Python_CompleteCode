class Organization:
    company = "Rayne Zone"

    def details(self):
        print(f"This is one of the Great Zone --->>{self.company}.")


class Employee(Organization):
    role = "Data Scientist"

    def details(self):
        print("I am happy.")


class Salary(Employee):
    def details(self):
        salary = "1000k"
        print(f"I am happy. My salary {self.salary}")


Org = Organization()
Org.details()

Emp = Employee()
Emp.details()

sal = Salary()
sal.details
