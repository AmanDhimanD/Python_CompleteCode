class programmer:
    company="Facebook"

    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getInfo(self):
        print(f"The name of {self.company} programmer is {self.name} and the product is {self.product}.")

Rayne=programmer("Rayne","MsTeam")
Ram=programmer("Ram","YouTuber")

Rayne.getInfo()

Ram.company="GitHub"
Ram.getInfo()

