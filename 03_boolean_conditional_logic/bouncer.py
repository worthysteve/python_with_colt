# ask for age
age  = int(input("How old are you?\n"))

# if age:
# 	# 18-21 wristband
# 	if age >= 18 and age < 21:
# 		print("You can enter, but need a wristband.")
# 	# 21+ drink, normal entry
# 	elif age >= 21:
# 		print("You are good to enter and can drink!🍾")
# 	# too younf, sorry
# 	else:
# 		print("You can't come in, little one!😞")
# else:
#     print("Please enter an age!")
    
# if age and (age >= 18 and age < 21):
#     print("You can enter, but need a wristband.")
# elif age and age >= 21:
#     print("You are good to enter and can drink!🍾")
# else:
#     print("You can't come in, little one!😞")

if age:
    if age >= 21:
        print("You are good to enter and can drink!🍾")
    elif age >= 18:
        print("You can enter, but need a wristband.")
    else:
      print("You can't come in, little one!😞")
else:
    print("Please enter an age!")