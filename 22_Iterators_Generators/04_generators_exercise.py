"""
! Week Generator Exercise
Write a function called week, which returns a generator that yields each day of the week, starting with Monday and ending with Sunday.  After Sunday, the generator is exhausted.  It does not start over.
"""

'''
days = week()
next(days) # 'Monday'
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration
'''

'''
Week Generator Solution
Define the generator function week  which has a list of days.  Iterate over the days and yield each day.   After "Sunday", the generator is exhausted.  It does not start over.
'''

def week():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    for day in days:
        yield day

# Instantiate the generator
days = week()

# Testing the generator using next()
print(next(days))  # 'Monday'
print(next(days))  # 'Tuesday'
print(next(days))  # 'Wednesday'
print(next(days))  # 'Thursday'
print(next(days))  # 'Friday'
print(next(days))  # 'Saturday'
print(next(days))  # 'Sunday'
# The next call will raise StopIteration, because the generator is exhausted