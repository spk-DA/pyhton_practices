# ============================================================
#              2. DECISION-MAKING STATEMENTS
# ============================================================
# Use if, if-else, and if-elif-else wherever appropriate.
# Basic Decision-Making


# 1. Check whether a number is positive or negative.

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 2. Check whether a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Check whether a person is eligible to vote.

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 4. Find the greater of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both numbers are equal")


# 5. Check whether a student has passed or failed.
# Passing marks are 40.

marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# 6. Check whether a number is divisible by 5.

num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")


# 7. Check whether a person is eligible for a driving license.

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")


# 8. Display a grade based on the student's marks:
# 80–100 → A
# 60–79 → B
# 40–59 → C
# Below 40 → Fail

marks = int(input("Enter marks: "))

if marks >= 80 and marks <= 100:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")


# 9. Check whether a given year is a leap year.

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# 10. Create a simple calculator using +, -, *, and /.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
symbol = input("Enter operator (+, -, *, /): ")

if symbol == "+":
    print("Addition is", a + b)

elif symbol == "-":
    print("Subtraction is", a - b)

elif symbol == "*":
    print("Multiplication is", a * b)

elif symbol == "/":
    if b != 0:
        print("Division is", a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Symbol is not valid")
