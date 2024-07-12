# discussed in class, Mon 31 jan. 2011.

# here is another way to read in
# info from a file.

# this program prompts the user for a
# filename and then prints out the
# content of that file in all caps

filename = input("Please input a filename:")

infile = open( filename, mode="r")

for line in infile:
    # process the file line by line

    print(line[:-1], "!", sep="", end="\n")
    #caps = line.upper()
    #print(caps, end="")

# close the file
infile.close()


