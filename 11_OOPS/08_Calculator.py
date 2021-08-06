class Calculator:
    def __init__(self,num):
        self.num=num

    def Square(self):
        # pass 
        print(f"The Sqaure of {self.num} is {self.num**2}.")
    def SquareRoot(self):
        print(f"The Sqaure Root of {self.num} is {self.num**0.5}.")
        
    def Cube(self):
        print(f"The Cube of {self.num} is {self.num**3}.")

Number=Calculator(3)
Number.Square()
Number.SquareRoot()
Number.Cube()