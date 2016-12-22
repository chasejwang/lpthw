def cheese_and_cracker(cheese_count, boxes_of_cracker):
    print "You have %r cheeses!" %cheese_count
    print "You have %r boxes of crackers!" %boxes_of_cracker
    print "Man, that's enough for a party."
    print "Get a blanket."

print "We can just give the function numbers directly."
cheese_and_cracker(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 66
amount_of_cracker = 88

cheese_and_cracker(amount_of_cheese,amount_of_cracker)

print "We can even do math inside too:"
cheese_and_cracker(19+31, 190+30)

print " And we can combine the two, variables and math:"
cheese_and_cracker(amount_of_cracker + 10, amount_of_cheese + 1000)
