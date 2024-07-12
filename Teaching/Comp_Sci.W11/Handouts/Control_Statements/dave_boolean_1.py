# Example from class
# 14 Feb 2011
# A program illustrating some
# things about Booleans and
# conditions and stuff

# Often one wants to check two
# conditional statements at once.
# This can frequently be done
# most simply with boolean logic,
# using "and" and "or"

def main():
    x = eval(input("Enter a number: "))
    y = eval(input("Enter a number: "))

    if x==0 and y ==0:
        print("Both numbers are zero")

    if x<0 or y<0:
        print("At least one of the numbers is negative")
    # note that A or B is true if one or both of
    # A and B are true.  This is different from how
    # "or" is used in everyday speech.
    # DF note to self: draw truth tables on board

    if x>0 or y>0:
        print("At least one of the numbers is positive")

    if not(x==0 and y==0):
        print("Neither of the numbers are zero.")
    # sometimes it is easier to check that something
    # isn't true.  the "not" statement can help

    if (x<0 and y<0) or (x>0 and y>0):
        print("Both numbers have the same sign")
    # note: when using multiple booleans,
    # use parentheses


 
main()
              

        
