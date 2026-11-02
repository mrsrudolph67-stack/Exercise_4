# Question 1
print ("Question 1")

fruits = ("Banana", "Apple", "Peach", "Grapes")

for fruit in fruits:
    print (fruit)

# Question 2
print ("Question 2")

count =  5

while count >= 1:
    print (count)
    count -= 1

# Question 3
print ("Question 3")

for number in range (1, 11):
    square = number ** 2
    print (square)

# Question 4
print ("Question 4")

import random 

colours = ("red", "green", "blue", "orange")

for i in range (3):
    colour = random.choice (colours)
    print (colour)

# Question 5
print ("Question 5")

import math_operations

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input ("Enter operator (+, -, *, /, %, **): ")

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Can't divide by zero"

elif operation == "*":
    result = num1 * num2

elif operation == "**":
    result = num1 ** num2

elif operation == "%":
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Error. Cannot Modulate by zero"

print ("Result: ", result)