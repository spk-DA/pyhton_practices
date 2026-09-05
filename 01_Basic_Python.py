# ============================================================
#                    1. BASIC PYTHON
# ============================================================
# Answer all 10 questions.


# 1. Write a Python program to print "Hello, Python!".

print("Hello, Python!")


# 2. Store your name, age, and city in variables and display them.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("Name:", name)
print("Age:", age)
print("City:", city)


# 3. Take two numbers from the user and display their sum.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

total = a + b

print("Sum:", total)


# 4. Take two numbers and display their addition, subtraction,
# multiplication, and division.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# 5. Write a program to calculate the area of a rectangle.

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area of rectangle:", area)


# 6. Write a program to calculate the area of a circle.

radius = float(input("Enter radius: "))

area = 3.14159 * radius * radius

print("Area of circle:", area)


# 7. Write a program to convert Celsius into Fahrenheit.

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)


# 8. Take a student's name and marks and display the details.

student_name = input("Enter student name: ")
marks = float(input("Enter marks: "))

print("Student Name:", student_name)
print("Marks:", marks)


# 9. Write a program to calculate Simple Interest
# using Principal, Rate, and Time.

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

simple_interest = principal * rate * time / 100

print("Simple Interest:", simple_interest)


# 10. Write a program to swap the values of two variables.

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

print("Before swap: a =", a, "b =", b)

a, b = b, a

print("After swap: a =", a, "b =", b)
