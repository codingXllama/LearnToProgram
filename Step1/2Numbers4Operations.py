# Ask the user to input 2 values and store them in varItem1 and VarItem 2

varNum1, varNum2 = input("Enter 2 numbers: ").split()

# now We convert the strings into regular number integers
varNum1 = int(varNum1)
varNum2 = int(varNum2)

# Add the values entered and store them in a variable called "sum"
sum = varNum1 + varNum2

# Subtract the values entered and store them in a variable called "subTract"
subTract = varNum1 - varNum2

# Multiply the values and store them in  a product variable
product = varNum2 * varNum1

# Divide the values and store in quotient
quotient = varNum1 / varNum2

# Use modulus on the values to find the reminder
remainder = varNum1 % varNum2

# Printing the results
# we format out data as such:
print("{}+{}={}".format(varNum1, varNum2, sum))
print("{}-{}={}".format(varNum1, varNum2, subTract))
print("{}*{}={}".format(varNum1, varNum2, product))
print("{}/{}={}".format(varNum1, varNum2, quotient))
print("{}%{}={}".format(varNum1, varNum2, remainder))
