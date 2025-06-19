#Create a Staff class in this file
#Accept and assign agreed parameters in the constructor and define agreed public methods in the class
#Program the class so that users of the class only need to interact with its methods
from person import Person

raise_amount= 0.04
class StaffPerson:
    def __init__(self, name, salary, amount):
        super().__init__(name)
        self.salary=salary
    def giveRaise(self, amount):
        current_salary= int(self.salary * Person.raise_amount)        

        
    def getSalary(self):
        return self.salary

        
        
