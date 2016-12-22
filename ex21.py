def add(a, b): # def is the defition function, in other way, tell the computer to do in the way you would like it to do.
    print "ADDING %d + %d"%(a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d- %d"%(a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" %(a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d"%(a, b)
    return a / b

print "Let's do some math with just function!"

age = add(30, 5) # here is the commmand function, which runs the function above.
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "age: %d,height: %d, Weight: %d, IQ: %d"% (age,height, weight, iq)

print "Here is a puzzle"

what = add (age, subtract(height, multiply(weight,divide(iq, 2))))

print "That becomes:", what,"Can you do it by hand?"
