# discussed in class, Wed 26 jan. 2011.

# example illustrating basic file input
# Note: File input is often a pain.  My
# experience is that it is never as easy
# as it seems.  But with python's nice
# string methods, it is easier than it
# used to be

infile = open( "sample.txt", mode="r")

# there are different ways to get the
# contents of the file into python's
# brain

# READ THE WHOLE FILE AT ONCE
# whole_thing = infile.read()

#print(whole_thing)
# whole_thing is now one large string
# you could split this into a list of
# words
#whole_thing_split = whole_thing.split()


# READ ONE LINE AT A TIME
#first_line = infile.readline()
#print(first_line[:-1])
#second_line = infile.readline()
#print(second_line)
#third_line = infile.readline()
#print(third_line)

# READ ALL, but put each line as
# an entry in a list
all_lines = infile.readlines()

for i in range(6):
    all_lines[i] = all_lines[i].split()

#print(all_lines)
#print(all_lines[2][3])

# now you have a big two-dimensional
# array, and you can access elements
# of this array as needed.

# close the file
# may not be necessary, but it's a
# good idea to close files
# before the program ends.
infile.close()
