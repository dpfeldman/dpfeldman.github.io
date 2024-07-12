# a snippet of code to check critical orbits for
# the M-set chapter
#
# March 24 2014


z = 0.0 + 0.0j
c= -0.157 + 1.031j
N = 60
print("t","\tz_t")
print(0,z)
for t in range(N):
    z = z*z +c
    print(t+1,z)


