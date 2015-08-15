#imports argv
from sys import argv

#enter script name, then file to read
#script, filename = argv

#new function open() that sets the contents of filename(passed from the run line) = txt variable
#txt = open(filename)

#does the read command on the next data that is the txt variable
#print "Here's your file %r:" % filename
#print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")



txt_again = open(file_again)

print txt_again.read()