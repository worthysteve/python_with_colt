# Totaling Donations Exercise
# Given the provided dictionary of donations:

# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0) 

# Use a loop to calculate the total value of the donations.  Save the result to a variable called total_donations 

# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!


# Use a loop to add together all the donations and store the resulting number in a variable called total_donations
total_donations = 0

for value in donations.values():
    total_donations += value
print(total_donations)


# Advanced Version 1 - 
# This solution uses a built-in function called sum() which I cover in the "Lambdas and Built-In Functions" section.   We haven't talked about how it works, but if you're curious...

total_donations = sum(donation for donation in donations.values())
print(total_donations)


# Advanced Version 2
# An even better solution using the same sum built-in function is just this nice little line:

total_donations = sum(donations.values())
print(total_donations)