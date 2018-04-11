def add(a,b):
    print("adding %d + %d" %(a,b))
    return a+b

def subtract(a,b):
    print("Subtracing %d- %d" %(a,b))
    return a-b

def multiply(a,b):
    print("Multiplying %d * %d" %(a,b))
    return  a*b

def divide(a,b):
    print("Dividing %d / %d" %(a,b))
    return a/b

print("Print the mathematics results with above functions")

age = add(30, 5)
height = subtract(80, 20)
weight = multiply(5, 16)
Iq = divide(20, 5)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, Iq))

print("Here is the puzzle")
what = add(age, subtract(height, multiply(weight, divide(Iq,2))))

print("That becomes ", what , " Can you do it by hand? ")