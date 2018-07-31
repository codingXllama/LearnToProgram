# Problem: Receive miles and convert to kilometers
# Kilometers = miles *1.60934
# Enter Miles 5
# 5 miles equals 8.04 kilometers

# Asking user to input miles (Taking user input as an integer)
userIn = int(input("Enter Miles "))
# printing the calculation of converting miles to km to the user
print(userIn, "is equal to {} kilometers ".format(userIn * 1.60934))
