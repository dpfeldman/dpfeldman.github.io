# numbers2text.py
# discussed in class 1/24/11
# based on program on page
# 137 of Zelle


print("This program converts a sequence of Unicode")
print("numbers into a string of text.")

inString = input("Enter a unicode-encoded message:")

message = "" # this will be the decoded message
# we start off with an empty string and then
# will concatentate characters to it

for numStr in inString.split():
    code_number = eval(numStr)
    message = message + chr(code_number)
    print(message)

print("The message is:", message)

# Note:  strings are objects!
# thus, they have methods associated
# with them.  split is one such method
# for others, see pate 140 of Zelle
