'''
import calendar

cal = calendar.month(2017, 9)
print("Here is the month", cal)
'''

import time

tim = time.asctime(time.localtime(time.clock()))
print("here is the current time", tim)