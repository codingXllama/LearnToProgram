# This program checks for how important is your birthday
# Purpose of this program is to  understand the purpose and usage of logical and/or operators , and multi if statements with the not keyword

# Getting user's age
userAge = eval(input("Enter your Age: "))
if userAge >= 1 and userAge <= 12:
    print("Your Birthday  is Important ")
elif userAge == 21 or userAge == 50:
    print("Your Birthday is Important !")

# We now check if the user age is less than 65 , then their birthday is important , else their birthday is not important
elif not userAge < 65:
    print("Your Birthday is Important!")
else:
    print("Your Birthday is Not Important :(")
