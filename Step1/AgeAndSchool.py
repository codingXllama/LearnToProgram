# Given the persons age , we will use societies standards to determine what education level they should belong to

# Asking for user's age
userAge = eval(input("Enter your age: "))
# if the user's age is 5
if userAge < 5:
    print("You're way too young for school !")
elif userAge == 5:
    print("You Go to Kindergarten")
# Since the student's age is between 6-17 , then we can check what is the actual grade they belong to using 1 condition

elif (userAge > 5) and (userAge <= 17):
    userGrade = userAge - 5  # example if userAge=6 , the this gives us 6-5=1 , where 1 is the grade of the person who is 6 years old
    print("You Go to grade {}".format(userGrade))
# This condition handles every student who is greater than 17
else:
    print("You Go to college")


