cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers # assuming that all drivers drive cars.
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
rockets = 10
space_in_a_rocket = 100.0
astros = 2
followers = 10000
rockets_not_launched = rockets - astros
rockets_launched = astros
rocketpool_capacity = rockets * space_in_a_rocket
average_passengers_per_rocket = followers / rockets
print "Is it true that followers / rockets > space_in_a_rocket?"

print followers / rockets > space_in_a_rocket

print "there are", cars, "cars available."
print "there are only", drivers, "drivers available."
print "there will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


print "we have", rockets, "rockets available to launch into the Mars."
print "But only", astros, " astrons can fly with necessary skills."
print "We have extra capacity of", rockets_not_launched, "rockets."
print "We have", followers, "followers to rocketpool today."
print "we only can to put about", average_passengers_per_rocket, "in each rocket."

print "there are %d cars available.:" % cars
