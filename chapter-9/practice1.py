# q1> create a class Car with attributes brand = "Scorpio"
class Car:
    brand = "Scorpio"

c1= Car()
print(c1.brand)

# q2> create class laptop with attributes: brand, RAM, price. 
# create 2 objects with different values

class Laptop:
    brand= "macbook" # class attribute
    RAM= "256 gb"
    price= "2 lakh"

l1 = Laptop()

l2= Laptop()

l2.brand = "ASUS" # instance attribute 
# We changed the atrribute value with help to object
l2.price = "50k"
l2.RAM = "512GB"

print(f"brand -> {l1.brand}, RAM -> {l1.RAM}, price -> {l1.price}")
print(f"brand -> {l2.brand}, RAM -> {l2.RAM}, price -> {l2.price}")

# note -> Instance attribute has more value/weightage than class attribute

    