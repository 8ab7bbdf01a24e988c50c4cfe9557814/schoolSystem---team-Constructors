#Create a Task class in this file
#Accept and assign agreed parameters in the constructor and define agreed public methods in the class
#Program the class so that users of the class only need to interact with its methods

class Task:
  def __init__(self, name, maxMark):
    self.name=name
    self.maxMark=maxMark
    self.marks=marks
    print(f"Created task {self.info()}")
  
  def info(self):
    return f"{self.name} maxMark={self.maxMark} #marks={len(self.marks)} max={self.maxMark}."
  
  def getName(self):
    return self.name

  def getMaxMark(self):
    return self.maxMark

  def setMark(self, student, mark):
    self.marks[student]=mark
    
