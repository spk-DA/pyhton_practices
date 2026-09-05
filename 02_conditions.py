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
    
# ============================================================
#                  MENU-DRIVEN QUESTIONS
# ============================================================


# 11. Create a menu-driven program to perform the following operations:
# 1 → Addition
# 2 → Subtraction
# 3 → Multiplication
# 4 → Division

print("1 → Addition")
print("2 → Subtraction")
print("3 → Multiplication")
print("4 → Division")

choice = int(input("Enter your choice: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Addition:", a + b)

elif choice == 2:
    print("Subtraction:", a - b)

elif choice == 3:
    print("Multiplication:", a * b)

elif choice == 4:
    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice")


# 12. Create a menu-driven program for a student:
# 1 → Display Student Name
# 2 → Display Student Marks
# 3 → Display Student Grade

student_name = input("Enter student name: ")
marks = int(input("Enter student marks: "))

print("1 → Display Student Name")
print("2 → Display Student Marks")
print("3 → Display Student Grade")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Student Name:", student_name)

elif choice == 2:
    print("Student Marks:", marks)

elif choice == 3:
    if marks >= 80:
        print("Grade: A")
    elif marks >= 60:
        print("Grade: B")
    elif marks >= 40:
        print("Grade: C")
    else:
        print("Grade: Fail")

else:
    print("Invalid choice")


# 13. Create a menu-driven program for a basic banking system:
# 1 → Check Balance
# 2 → Deposit
# 3 → Withdraw

balance = 10000

print("1 → Check Balance")
print("2 → Deposit")
print("3 → Withdraw")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Current Balance:", balance)

elif choice == 2:
    deposit = float(input("Enter deposit amount: "))

    if deposit > 0:
        balance = balance + deposit
        print("Deposit successful")
        print("Current Balance:", balance)
    else:
        print("Invalid deposit amount")

elif choice == 3:
    withdraw = float(input("Enter withdrawal amount: "))

    if withdraw <= 0:
        print("Invalid withdrawal amount")
    elif withdraw > balance:
        print("Insufficient balance")
    else:
        balance = balance - withdraw
        print("Withdrawal successful")
        print("Current Balance:", balance)

else:
    print("Invalid choice")


# 14. Create a menu-driven program to calculate:
# 1 → Area of Rectangle
# 2 → Area of Circle
# 3 → Area of Square

print("1 → Area of Rectangle")
print("2 → Area of Circle")
print("3 → Area of Square")

choice = int(input("Enter your choice: "))

if choice == 1:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    area = length * width

    print("Area of Rectangle:", area)

elif choice == 2:
    radius = float(input("Enter radius: "))

    area = 3.14159 * radius * radius

    print("Area of Circle:", area)

elif choice == 3:
    side = float(input("Enter side: "))

    area = side * side

    print("Area of Square:", area)

else:
    print("Invalid choice")


# 15. Create a menu-driven program to convert:
# 1 → Celsius to Fahrenheit
# 2 → Fahrenheit to Celsius

print("1 → Celsius to Fahrenheit")
print("2 → Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))

try:
    temperature = float(input("Enter temperature: "))

    if choice == 1:
        fahrenheit = (temperature * 9 / 5) + 32
        print("Temperature in Fahrenheit:", fahrenheit)

    elif choice == 2:
        celsius = (temperature - 32) * 5 / 9
        print("Temperature in Celsius:", celsius)

    else:
        print("Input value is invalid")

except ValueError:
    print("Error: Please enter numbers only.")










