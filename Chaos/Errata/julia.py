# a snippet of code to check Eq. 24.5 in the Chaos Textbook
#
# March 23 2014


z = 0.8 + 0.2j

print("t","\tz_t")
print(0,z)
for t in range(20):
    z = z*z - 1
    print(t+1,z)


