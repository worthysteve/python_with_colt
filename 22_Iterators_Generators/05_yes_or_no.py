
"""
! yes_or_no
Write a function called yes_or_no, which returns a generator that first yields yes , then no , then yes , then no , and so on."""

"""
* Yes Or No Generator Solution
yes_or_no  loops forever (while True) and yields answer , and then toggles answer from yes to no, or vice versa.
"""

def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"

# Instantiate the generator
gen = yes_or_no()

# Testing the generator using next()
print(next(gen))  # 'yes'
print(next(gen))  # 'no'
print(next(gen))  # 'yes'
print(next(gen))  # 'no'