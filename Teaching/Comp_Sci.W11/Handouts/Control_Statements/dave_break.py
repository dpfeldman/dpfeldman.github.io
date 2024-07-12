# Example from class
# 14 Feb 2011
# A program illustrating the
# use of the break command
# to exit a loop

# See Zelle, 8.5.1-2


def average_1():
   # here is one way of implementing a simple
   # average program
   # note that we need to ask the question
   # outside of the loop to get things started
    sum = 0
    counts = 0
    n = input("Enter a number <enter> to quit: ")
    while(n !=""):
        sum = sum + eval(n)
        counts = counts + 1
        n = input("Enter a number <enter> to quit: ")

    print("Total =", sum, "\tAverage =", sum/counts)

        
def average_2():
   # here is another way to implement the
   # same program
    sum = 0
    counts = 0
    while(True):
        n = input("Enter a number <enter> to quit: ")
        if(n):
            sum = sum + eval(n)
            counts = counts + 1
        else:
            break
        
    print("Total =", sum, "\tAverage =", sum/counts)

#note the use of the break command.

# here are two more examples of a simple program
# that checks to see if input is positive

def check_1():
    n = -1 # set to illegal value to enter loop
    while(n<=0):
        n = eval(input("Enter a positive number: "))
        if n<=0:
            print("Pay attention.  You didn't enter a positive number.")
    print("Nice job.  You correctly entered a positive number.")

# the same program, but with a break statement
def check_2():
    while(True):
        n = eval(input("Enter a positive number: "))
        if n<=0:
            print("Pay attention.  You didn't enter a positive number.")
        else:
            break
    print("Nice job.  You correctly entered a positive number.")


# which approach is better?  should you use breaks?
# this is largely a matter of style.  aim for clear
# and readable code.  but be aware that many coders
# use breaks quite frequently.
