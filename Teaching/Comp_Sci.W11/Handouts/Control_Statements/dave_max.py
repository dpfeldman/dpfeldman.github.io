# 10 Feb. 2011
# this program defines a bunch
# of different max functions
# these examples follow those from
# Chapter 7.5 of Zelle

# this program doesn't actually
# do anything, it just defines the
# functions.  test the functions
# from the command line

# you might want to add a few notes
# to this file as we go over it
# in class...

def max_A(x1, x2, x3):
    if x1 >= x2 and x1 >= x3:
        return x1
    elif x2 >= x1 and x2 >= x3:
        return x2
    else:
        return x3

def max_B(x1, x2, x3):
    if x1 >= x2:
        if x1 >= x3:
            return x1
        else:
            return x3
    else:
        if x2 >= x3:
            return x2
        else:
            return x3

def max_C(x1, x2, x3):
    max = x1
    if x2 > max:
        max = x2
    if x3 > max:
        max = x3
    return max


