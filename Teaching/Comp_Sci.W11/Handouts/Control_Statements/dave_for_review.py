# 10 Feb 2011
# this program reviews for loops

def main():
    # most often we have used for
    # loops like this
    for i in range(5):
        print(i)
    print()
    # this is a definite loop
    # it does something a definite
    # number of times

    # range(5) is an implicit
    # list
    print("list(range(5)) = ",list(range(5)))
    print()

    # for loops can loop through
    # other types of lists
    for i in [3, 4, 8, 4]:
          print(i)

    # loop through a string
    ok = "lumberjack"
    for ch in ok:
        print(ch, end="")
    print("\n")

    # loop through a list
    names = ["alice", "bob", "chris"]
    for str in names:
        print(str)
    print()

main()   
