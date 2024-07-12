# one more function example
# 8 Feb 2011
# this program reviews the stuff we did
# with functions last week

# Key points
#
# 1.  function calls must match their
#     definition
# 2.  functions can return a value
#     and can take multiple parameters
#     as input
# 3.  scope is confusing.  a function
#     only knows about local variables,
#     things that are passed as a parameter
#     to it.  a function cannot changes
#     the values of variables in main()
# 4.  however, if you pass a list as an
#     argument to a function, it *can*
#     change the elements in the list


def bogus_double(x):
    # this function looks like it
    # will double x, but it doesn't
    x = 2*x
    
# a correct way to have a doubling function
def double(x):
    return (2*x)


# *+*+*+*+* BEGIN REVERSE FUNCTION *+*+*+*+*
# this function takes a list of three
# numbers as a parameter. it then puts the
# elements in the list in reverse order
def reverse(list):
    # figure out how long the list is
    N = len(list)
    # make copy of list
    copy = [] #makes empty list
    for i in range(N):
        copy.append(list[i])

    # now reverse it
    for i in range(N):
        list[i] = copy[N-1-i]
# *+*+*+*+* END REVERSE FUNCTION *+*+*+*+*


def main():
    x = 13
    print("x =", x)
    bogus_double(x)
    print("after bogus_double, x =", x)
    x = double(x)
    print("after non-bogus double, x =", x)
    print()
    numbers = [ 4, 5, 6, 7, 8, 9]
    print("List is:", numbers)
    reverse(numbers)
    print("After reversal, list is:", numbers)
main()

# what do you think will happen when this
# program is run.  why??

# note to self.  if time, discuss programming
# style, functions, lines lengths, paragraphs
# etc.
