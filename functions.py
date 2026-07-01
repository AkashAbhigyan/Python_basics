def square(number):
    square = number ** 2
    return square
input1 = int(input("Enter a number to find its square: "))
print("The square of the number is:", square(input1))

def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
input2 = int(input("Enter a number to check if it's even or odd: "))
print("The number is:", even_odd(input2))

def maximum(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both numbers are equal"
input3 = float(input("Enter the first number: "))
input4 = float(input("Enter the second number: "))
print("The greater number is:", maximum(input3, input4))

def name(person_name):
    return "Hello, " + person_name + "!"
input5 = input("Enter your name: ")
print(name(input5))

def circle_area(radius):
    area = 3.14159 * (radius ** 2)
    return area
input6 = float(input("Enter the radius of the circle: "))
print("The area of the circle is:", circle_area(input6))