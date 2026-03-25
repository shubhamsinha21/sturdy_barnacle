# Attributes

class Student:
    
    def __init__(self, name, course):  # init function -> constructor
        # self -> jis object ke lye init hai whi pass hota hai yaha pe self me
        # print(self)
        # print("whenever a new object is created, i'm called automatically")
        self.name = name # we are declaring that self attribute has name -> same as student name
        self.course = course
        
Student1 = Student("khushi", "btech") # init method will be called, when object is created
print("\nStudent1 name -> ", Student1.name )
print("Student1 course -> ", Student1.course)

Student2 = Student("Ankit", "bsc")
print("\nStudent2 name -> ", Student2.name )
print("Student2 course -> ", Student2.course)
        
# Methods

class Student:
    name= "shubham" # attribute
    
# creating object
s1 = Student()
print("\nname ->",s1.name)

class Vehicle:
    color= "black"
    petrolDiesel= 'petrol'
    mileage= 12.5
    
    def start():
        print("When you press clutch, car starts")

# object creation -> CREATED 3 OBJECTS and one class

car = Vehicle()
bike = Vehicle()
aeroplane = Vehicle()
print(car.mileage)
print(aeroplane.color)
print(bike.petrolDiesel)
# print(Vehicle.start())

        