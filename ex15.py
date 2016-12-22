from sys import argv #sys is a package. this phrase just says to get the (argv) feature from that package.
#
script, filename = argv # input infor

txt = open(filename) #text opening function

print "Here's your file %r:" % filename  # print the decription with the name of files
print txt.read() # print that text info that you input to request

print "Type the filename again:"  # the system talking
file_again = raw_input("> ") # request for input with raw_input function

txt_again = open(file_again) # text openning function

print txt_again.read()
 # txt.read() says: Hey, txt! do you read commnad with no parameters.

# asking for help: searching online for "python THING" OR "python open"
