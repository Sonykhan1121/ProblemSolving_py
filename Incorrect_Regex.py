import re

# Number of test cases
tc = int(input(""))
while tc > 0:
    # Read regex pattern
    s = input()
    try:
        # Try to compile the pattern
        re.compile(s)
        print("True")
    except re.error:
        print("False")
    
    # Decrement the test case counter
    tc -= 1
