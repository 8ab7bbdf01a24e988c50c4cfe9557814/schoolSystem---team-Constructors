#Create a Staff class in this file
#Accept and assign agreed parameters in the constructor and define agreed public methods in the class
#Program the class so that users of the class only need to interact with its methods

from person import Person

class Staff(Person):
    raise_amount = 0.04  # Class variable for raise percentage

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def give_raise(self):
        self.salary = int(self.salary * (1 + self.raise_amount))

    def get_salary(self):
        return self.salary
        
        
