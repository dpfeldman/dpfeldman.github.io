# feb 10, 2011
# a few examples of while loops

def main():

    # a simple example of a while loop
    i = 0
    while(i<5):
        print(i)
        i = i+1
    #DF: note to self.  try different
    #    ways of breaking this

    # for the above example a for
    # loop actually makes more sense
    # since you know from the start
    # how many iterations you want
    # while loops are used when you
    # might want to loop a different
    # number of times depending on
    # the circumstances

    # calculate doubling time of
    # an investment
    r = eval(input("Enter Interest rate:"))
    money = 100
    years = 0
    while(money < 200):
        money = money*(1+r)
        years = years +1

    print("The doubling time is approx",
          years, "years")
    
    
    

main()
