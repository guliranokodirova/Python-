def leap_year(year):
     
    if not isinstance(year,int):
      raise ValueError('Year must be an integer type')

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

try:
   year = int(input('Please enter a year: '))

   #checking if the yaer is a leap year 
   if leap_year(year): 
    print(f'{year} is leap year')
   else: 
    print(f'{year} is not leap year')

except ValueError as e: 
 print(f'Error: {e}')


 #n is odd not odd 
#Если n нечетное, выведите "Странно"

#Если n четное и в пределах от 2 до 5 включительно, выведите "Не странно"

#Если n четное и в пределах от 6 до 20 включительно, выведите "Странно"

#Если n четное и больше 20, выведите "Не странно"


n = int(input("Enter any number: "))
 
if n % 2 != 0 : 
        print('Weird')
elif n % 2 == 0 and 2 <= n <= 5:
        print('Not weird')
elif n % 2 == 0 and 6 <= n<= 20 :
        print('Weird')
elif n % 2 == 0 and n > 20: 
        print('Not weird')
else:
        print('Not identified yet')



# given two numbers a and b, find even numbers between those two, both are inclusive: 
a = int(input("Insert first value: "))
b = int(input("Insert second value: "))

#first solution 

for even_number in range(a-1,b+1):
    if even_number % 2 == 0: 
      print(even_number)

  

    

#second solution 
even_num = list(filter(lambda x: x % 2 == 0, range(a-1, b+1)))
print(even_num)
   
