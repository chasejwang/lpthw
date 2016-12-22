from sys import argv

script, user_name = argv
prompt = "<"

print "Hi %s, I'm the %s script" % (user_name, script)
print "I'd like to ask you a few questions"
print "Do you ike me, %s?" % user_name
like = raw_input(prompt)

print "Where do you live,%s?" % user_name
live = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
alright, so you said %r about like me.
you live in %r. No sure where that is.
and you have a %r computer. Nice
""" % (like, live, computer)
