
# 10 Feb 2011
# an example of an EOF loop
# see section 8.3.3 of Zelle

def main():
    infile = open("data.txt", 'r')
    sum = 0
    count = 0
    line=infile.readline()
    # reads in just one line of the file
    while (line != ""):
        sum = sum + eval(line)
        count = count + 1
        line = infile.readline()

    print("Total = ", sum)
    print("Average = ", sum/count)

main()
