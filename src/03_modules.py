"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for arguments in sys.argv:
    print(str(arguments)) #don't have to cast can just do print(arguments)


# Print out the OS platform you're using:
# YOUR CODE HERE
print("The OS platform I am using is: " + sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("The version of Python I am using is: " + sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("The current process ID is " + str(os.getpid()))

# Print the current working directory (cwd):
# YOUR CODE HERE
print("The current working directory is " + os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("This machine's login name is " + os.getlogin())