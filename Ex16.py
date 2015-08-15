from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w+')

print "Truncating the file..."
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

'''
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''

write_new = line1+"\n"+line2+"\n"+line3+"\n"

target.write(write_new)

target.close()

print "Here it is for verification:"
verify = open(filename)
print verify.read()

print "\n"
print "And now we close"
verify.close()
