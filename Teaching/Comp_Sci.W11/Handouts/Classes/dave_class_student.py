# here is an example program where we define our own classes
# discussed in class 17 feb 2011

# let's imagine that we want to keep track of students and
# courses.  perhaps we are writing registration software,
# or maybe we want to simulate the registration process

# you might want to add some comments to this as we discuss
# it in class

# Define the student class

class Student:

    def __init__(self, first_name, last_name):
        self.level = 1 #start as a first-year student
        self.standing = True #start in good academic standing
        self.first_name = first_name
        self.last_name = last_name

    def print_report(self):
        print("Student", self.first_name, self.last_name, "is ", end="")
        if(self.standing != True):
            print("not ", end="")
        print("in good academic standing.")
        print("Student level is:", self.level,"\n")

    def put_on_probation(self):
        self.standing = False

    def put_off_probation(self):
        self.standing = True

    def increment_level(self):
        self.level = self.level + 1

    def get_level(self):
        return self.level


def main():
    s1 = Student("Al", "Anderson")
    s1.print_report()
    s1.put_on_probation()
    s1.print_report()
    s1.put_off_probation()
    s1.print_report()
    s1.increment_level()

    print("The level is:", s1.get_level() ,"\n\n")

    s2 = Student( "Bob", "Boughner")
    s3 = Student( "Chris", "Carpenter")

    student_list = [s1, s2, s3]
    for s in student_list:
        s.print_report()

    # Exercise:
    # Write a member function that changes a student name

    # Exercise:
    # Write some code in main() that figures out the average
    # student level.
main()
