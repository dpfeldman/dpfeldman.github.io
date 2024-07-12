# feb 10 2011
# an example showing
# a "sentinel" loop
#

# a simple program that lets the
# user enter an arbitrary number
# of numbers and then calculates
# the sum and the average
def main():
    sum = 0
    count = 0
    n = eval(input("Enter a number (negative to quit):"))
    while(n>0):
        sum = sum + n
        count = count + 1
        n = eval(input("Enter a number (negative to quit):"))

    print("Total =", sum)
    print("Average = ", sum/count)


# here is another, slightly nicer version
# of this program

def main_2():
    sum = 0
    count = 0
    nStr = input("Enter a number (<Enter> to quit)")
    while(nStr!=""):
        sum = sum + eval(nStr)
        count = count + 1
        nStr = input("Enter a number (<Enter> to quit)")

    print("Total = ", sum)
    print("Average = " ,sum/count)


main()
