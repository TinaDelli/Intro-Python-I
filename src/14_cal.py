"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

curr_date = datetime.now()
curr_month = curr_date.month
curr_year = curr_date.year

# for args in sys.argv:
#   print(sys.argv)
# print(curr_date.month, curr_date.year)
# print(calendar.month(curr_year, curr_month))

def calen_program(arg1= curr_year, arg2= curr_month):
  print(calendar.month(arg1, arg2))

if len(sys.argv)-1 == 0:  #if no arguments
  calen_program()
elif len(sys.argv)-1 == 1: #if one argument
  calen_program((curr_year), int(sys.argv[1]))
else:  #if both arguments
  calen_program(int(sys.argv[2]), int(sys.argv[1]))

