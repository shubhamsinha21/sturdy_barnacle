# create class student that takes 3 marks and has a method average()
class Student():
    
    def __init__(self, name, phy, che, math):
        self.name = name
        self.phy = phy
        self.che = che
        self.math = math
    
    @staticmethod # -> if we use it, we dont need to write self inside method    
    def average(self):
        sum = 0
        sum = self.phy + self.che + self.math
        average = sum / 3
        print("\nAverage is: ", average)
        

    
student1 = Student('shubham', 45, 60, 90)
print("\nstudent1 marks in phy ->", student1.phy)
print("\nstudent1 marks in phy ->", student1.che)
print("\nstudent1 marks in phy ->", student1.math)

student1.average()
        
        