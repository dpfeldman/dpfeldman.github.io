# text2number.py
# a program that converts a text message
# into a sequence of numbers
# based on the program on p. 134 of Zelle

message = input("Enter a message to encode: ")

print("\nHere is your message in unicode (or ASCII):")

# loop through the message
# note that the string message
# is really a list, just like range(n)
for ch in message:
    print(ord(ch), end=' ')
    # the end=" " makes it so that
    # the print statement ends in a
    # space and not a newline
print("\n")
# \n is a new line
