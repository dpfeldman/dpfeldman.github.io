# 9 February 2011
# the first of several programs
# that illustrates various
# flavors of if statements

# ********************************************
# Testing for an equality
def main_0():
    n = eval(input("Please enter a number: "))
    if (n!=10):
        print("Your number is not ten!")
        print("This is a boring program.")
# Note the "=="!!
# DF note to self: discuss *conditions*
main_0()
# ********************************************

# ********************************************
def main_1():
    n = eval(input("Please enter a number: "))
    if(n>10):
        print("your number is larger than 10.")
# this is not ideal, since nothing happens
# if n is not more than 10
main_1()
# *********************************************

# *********************************************
def main_2():
    n = eval(input("Please enter a number: "))
    if(n>10):
        print("Your number is larger than 10.")
    if(n<=10):
        print("Your number is not larger than 10.")
# this program is redundant.  we check the n>10
# condition twice
main_2()
# *********************************************

# *********************************************
# this function illustrates the use of the
# if ... else construction
def main_3():
    n = eval(input("Please enter a number: "))
    if(n>10):
        print("Your number is larger than 10.")
    else:
        print("Your number is not larger than 10.")
# DF note to self: illustrate this with a
# flowchart
main_3()
# **********************************************

# **********************************************
# deciding among multiple options
def main_4():
    n = eval(input("Please enter a number: "))
    if(n>10):
        print("Your number is larger than 10.")
    elif (n==10):
        print("Your number is exactly 10.")
    else:
        print("Your number is less than 10.")
main_4()
# ***********************************************
