
# list_manipulation
# Write a function called list_manipulation. This function should take in four parameters (a list, command, location and value).

# If the command is "remove" and the location is "end", the function should remove the last value in the list and return the value removed
# If the command is "remove" and the location is "beginning", the function should remove the first value in the list and return the value removed
# If the command is "add" and the location is "beginning", the function should add the value (fourth parameter) to the beginning of the list and return the list
# If the command is "add" and the location is "end", the function should add the value (fourth parameter) to the end of the list and return the list

def list_manipulation(lst, comd, loc, val=None):
    if comd == 'remove' and loc == 'end':
        return lst.pop()
    elif comd == 'remove' and loc == 'beginning':
        return lst.pop(0)
    elif comd == 'add' and loc == 'beginning':
        lst.insert(0, val)
        return lst
    elif comd == 'add' and loc == 'end':
        lst.append(val)
        return lst

# Testing the function
print(list_manipulation([1,2,3], "remove", "end")) # Output: 3
print(list_manipulation([1,2,3], "remove", "beginning")) # Output: 1
print(list_manipulation([1,2,3], "add", "beginning", 20)) # Output: [20, 1, 2, 3]
print(list_manipulation([1,2,3], "add", "end", 30)) # Output: [1, 2, 3, 30]
