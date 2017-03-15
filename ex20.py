# import argv from sys
from sys import argv

# Scriptname + argument which is name of textfile
script, input_file = argv

# Function print_all that takes argument f, which should be a file
def print_all(f):
# Read / print all of file f
    print f.read()

# Function that goes back to line 0?
def rewind(f):
    f.seek(0)

# Function that prints a line, takes number of line and filename as argument
def print_a_line(line_count, f):
    print line_count, f.readline(),

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
#print "current_line is %r" % current_line
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1
#print "current_line is %r" % current_line
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1
#print "current_line is %r" % current_line
print_a_line(current_line, current_file)

