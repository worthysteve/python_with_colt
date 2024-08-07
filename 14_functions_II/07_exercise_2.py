
# **kwargs Exercise
# Note: for this exercise, make use of **kwargs.  No default parameters allowed!

# Write a function called combine_words  which accepts a single string called word and any number of additional key word arguments.  If a prefix is provided, return the prefix followed by the word.  If a suffix is provided, return the word followed by the suffix.  If neither is provided, just return the word.  It might sound confusing, but the examples should make this a lot clearer!

# combine_words("child")  #'child'

# combine_words("child", prefix="man")  #'manchild'

# combine_words("child", suffix="ish")  #'childish'

# combine_words("work", suffix="er")  #'worker'

# combine_words("work", prefix="home")  #'homework'

# Define combine_words below:
def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

print(combine_words("child"))
print(combine_words("child", prefix="man"))
print(combine_words("child", suffix="ish"))
print(combine_words("work", suffix="er"))
print(combine_words("work", prefix="home"))