#Create a Student class in this file
#Accept and assign agreed parameters in the constructor and define agreed public methods in the class
#Program the class so that users of the class only need to interact with its methods

#kate was herez😵

from person import Person

class Student(Person):
    test = 1
    def __init__(self, name, schoolYear):
        super().__init__(name)
        self.schoolYear=schoolYear        
    
    def getSchoolYear(self, schoolYear):
        return self.schoolYear
     
    def setSchoolYear(self, schoolYear):
        current_year=input("Set school year: ")
        
    def nextSchoolYear(self, schoolYear):
        next_year=current_year+1
        print(f"{self.Person} is gonna be in year {next_year} next year")
      
