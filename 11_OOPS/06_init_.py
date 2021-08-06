"""  
__init__ is a constractor
"""
class studentInfo:
    company="Google"
    def __init__(self,name,salary,job):
        self.name=name
        self.salary=salary
        self.job=job

    def printInit(self):
        print(f"Name is {self.name}.")
        print(f"Salary is {self.salary}.")
        print(f"Job at {self.job}.")

Rayne=studentInfo("Rayne",1000000,"Youtuber")
Rayne.printInit()
