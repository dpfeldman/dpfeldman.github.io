# Example from class
# 14 Feb 2011
# A program illustrating some
# more things about Booleans

# expressions can also be Booleans
# this is handy, but potentially
# confusing.  See Zelle, 8.5.3

# expressions like "hello" and
# 3+4 and 98.4 all can be converted to
# boolean expressions.  to illustrate
# this, try the following on the
# command line:
# bool(0)
# bool(1)
# bool(3.1415)
# bool("unladen swallow")
# bool("")
# bool(["spam", "spam", "SPAM"])
# bool([])

def question():
    ans = input("What flavor do you want [chocolate]: ")
    if ans: # this can be rewritten using
        # ans as boolean
        flavor = ans
    else:
        flavor = "chocolate"
    print("You want", flavor, "ice cream.\n")

def main():
    response = input("Do you want to answer a question? ")
    if ( (response[0] == 'y') or (response[0] == 'Y') ):
        question()
    response = input("Do you want to answer a question? ")
    if ( (response[0] == 'y') or ('Y')  ): #<-- this doesn't work!
        question()
    # why doesn't the second if statement do what
    # it looks like it should do??
 
main()

# so expressions can be used as booleans
# in control statements.  at first this may
# be confusing, but it is actually pretty
# handy.  it is also very common, and so you
# may encounter it in other code, in both
# python and other languages

# here is another example
def main_2():
    VERBOSE = 1 # if !0 then turn on verbose mode
    # if I am using a variable as a boolean I sometimes
    # put it in all caps

    sum = 0
    counts = 0
    n = input("Enter a number <enter> to quit: ")
    while(n !=""):
        sum = sum + eval(n)
        counts = counts + 1
        if(VERBOSE):
            print("counts: ", counts, "\tcurrent n:", n, "\tsum: ", sum)
        n = input("Enter a number <enter> to quit: ")

    print("Total =", sum, "\tAverage =", sum/counts)

        
