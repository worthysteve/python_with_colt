# return_day
# Write a function called return_day. this function takes in one parameter (a number from 1-7) and returns the day of the week (1 is Sunday, 2 is Monday, 3 is Tuesday etc.). If the number is less than 1 or greater than 7, the function should return None

# Hint: store the days of the week in a list (or dict using numbers as keys).

'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''

def return_day(num):
    days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }
    
    return days.get(num, None)

print(return_day(1)) 
print(return_day(2)) 
print(return_day(3)) 
print(return_day(4)) 
print(return_day(5)) 
print(return_day(6)) 
print(return_day(7)) 

print("=============================================================================")
def return_day(num):
    """Returns the day of the week corresponding to the given day number (1-7).
    
    Args:
        num (int): A number from 1 to 7 representing the day of the week.
        
    Returns:
        str: The name of the day corresponding to the given number.
        None: If the number is less than 1 or greater than 7.
    """
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    days = {i + 1: day for i, day in enumerate(days_of_week)}
    
    return days.get(num, None)

# Example usage:
print(return_day(1))  # Output: Sunday
print(return_day(4))  # Output: Wednesday
print(return_day(8))  # Output: None

print("=============================================================================")
# Here's a solution that uses what we've learned so far.  

# Keep track of the days in a list.  
# Check to make sure num isn't < 0 or  > 6.  
# Return the corresponding day. Use days[num-1] because return_day(1) should return 0th item in list.

def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None

print(return_day(1)) 
print(return_day(2)) 
print(return_day(3)) 
print(return_day(4)) 
print(return_day(5)) 
print(return_day(6)) 
print(return_day(7)) 

print("=============================================================================")
# BONUS ADVANCED VERSION:
# Here's a more advanced solution that involves error handling, which we have not covered yet.  It eliminates the need to check to see if num is a valid index in the list. We cover this in the debugging section, but I thought you may want to see if now.

def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None

print(return_day(1)) 
print(return_day(2)) 
print(return_day(3)) 
print(return_day(4)) 
print(return_day(5)) 
print(return_day(6)) 
print(return_day(7)) 