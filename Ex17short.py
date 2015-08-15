from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file, 'r').read(); newfile = open(to_file, 'w+');newfile.write(indata); newfile.close();

#open(to_file, 'w+').write(open(from_file, 'r').read()); to_file.close();



print "All done"
