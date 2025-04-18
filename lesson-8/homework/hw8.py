#1 ZeroDivisionError
try:
    x = 10/0
except ZeroDivisionError: 
    print('You can not divide by zero!')

#2
# ValueError
try:
    ent = int(input("Enter any num: "))
except ValueError:
    print("You must enter an intiger!")  

#3
#FileNotFounrError
try:
    with open("some_file.txt", "r") as a:
        content = a.read()
except FileNotFoundError:
    print("The file you are trying to open does not exist.")


#4
try:
    a = int(input("Enter a value for a"))
    b = input("Enter a value for b")
    a + b 
except TypeError:
    print('Error: You are trying to mix incompatible types')


#5
try:
    with open("restricted_file.txt", "w") as file:
        file.write("This is a test message.")
    print("File written successfully.")
except PermissionError:
    print("PermissionError: You do not have permission to write to this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

#6
try:
    ls = [ 1,2,3,4,5]
    print(ls[15])
except IndexError: 
    print("The list does not reach that index")

#7 KeyboardInteruptError
try: 
   num = 0 
   while num <  100000000000:
     print(num)
except KeyboardInterrupt:
   print("Error: You have been paused from running the function")

# 8 ArithmeticError 
def division(a, b):
    try:
        res = a / b
        print(f"The result of {a} divided by {b} is: {res}")
    except ArithmeticError:
        print("An arithmetic error occurred. Please check your input values.")
print(division(2,0))

#9 
try: 
    ls = [1,2,3,4]
    a = ls.keys
except AttributeError:
    print("Error: This object does not contain attribute that you have requested!")
