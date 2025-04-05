##Given a side of square. Find its perimeter and area.
side = int(input("Enter side of a square"))
def perimeter_calculator():
    answer = side * 4
    print(f"Perimeter of a square with side of {side} is {answer}") 
perimeter_calculator()

##Given diameter of circle. Find its length.
diameter=float(input("Enter the diameter of a square"))
def length():
    pi=3.14 
    print(pi*diameter)
length() 

##Given two numbers a and b. Find their mean.
a = float(input('give the value of (a): '))
b = float(input('give the value of (b): '))

mean = (a+b)/2 
print(mean)

##Given two numbers a and b. Find their sum, product and square of each number.
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

#define the sum
sum_ab = a + b
print(f"The sum of {a} and {b} is: {sum_ab}")

#define the product 
product_ab = a * b
print(f"The product of {a} and {b} is: {product_ab}")

#define the square 
square_a = a ** 2
square_b = b ** 2
print(f"The square of {a} is: {square_a}")
print(f"The square of {b} is: {square_b}")
