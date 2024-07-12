# initial example for chapter six
# discussed in class on Mon 31 Jan 2011

# this does the same thing as the previous
# program, dave_function_0.py, except now
# I've used functions

def happy():
    print("Happy birthday to you.")

def sing(name):
    happy()
    happy()
    print("Happy birthday dear", name + ".")
    happy()

sing("Alice")
print()
sing("Bob")
print()
sing("Chris")

# note to self: discuss formal parameters
# vs actual parameters

# the functions happy and sing have
# removed redundancy

# so far so good.  functions are pretty
# easy.  well ...
# except for a few tricky things
