# example discussed in class
# 26 january 2011
#

# this opens a file in write mode
output_file = open("output.dat", "w")

# output_file is now a file object

# If you are dealing with multiple
# files, then good file-naming
# conventions can be helpful

# the mode "w" erases the file before
# it starts writing to it
# if you want to append to the file
# instead of deleting it and starting
# anew, then use mode "a"

# now that the file is open, you
# can print to it just like you
# would print to the screen
print("Spam", file=output_file)

# it's a good idea to close the
# file before the program quits
output_file.close()
