from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

rich = raw_input ("how rich you are?")
age = raw_input ("how old are you?")

print "So, you have %r $, and %r years old." %(rich,age)
