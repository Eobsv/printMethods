name = "John"
age = 22
money = 10.75

#print using string concatentation
print(name + " is " + str(age) + " and has $" + str(money) + " dollars.")

#print using the .format() method for strings
print("{0} is {1} nad has ${2} dollars.".format(name, age, money))

#print using f-strings
print(f"{name} is {age} and has ${money} dollars.")