#1 Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math
class Circle:
    def __init__ (self,radius): 
        self.radius = radius

    def perimeter(self):
     per_cal= 2 * math.pi * self.radius 
     return per_cal
    def area(self):
     area_cal = math.pi * self.radius ** 2 
     return area_cal
onee = Circle(10)

print("Perimeter:" ,onee.perimeter())
print("Area:", onee.area())


#2 
class Person:
    pass
    def __init__(self,name,country, date_of_birth):
        self.name = name
        self.country= country
        self.date_of_birth = date_of_birth 

    def age(self):
        import datetime
        current_date = datetime.datetime.now()
        year = current_date.year
        birth_date = datetime.datetime.strptime("9/25/2007","%m/%d/%Y")
        birth_year = birth_date.year
        # print(birth_year)
        age = year - birth_year
        print(age)


person1 = Person('Gulirano', 'Uzbekistan', 9-25-2007)
person1.age()



#3 Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.
class Calculator:
    pass 
    def __init__(self, num_1,num_2):
      self.num_1 = num_1
      self.num_2 = num_2 

    def sum(self):
        a = self.num_1 + self.num_2 
        return a
    def minus(self):
        b = self.num_1 - self.num_2 
        return b
    def abc(self):
        c = self.num_1 * self.num_2 
        return c
    def power(self):
        d = self.num_1 ** self.num_2 
        return d
    
operation = Calculator(2,3)
   
print("Sum:",operation.sum())
print("minus:",operation.minus())
print(":",operation.abc())
print("multiplication:",operation.power())




#4 
import math 
class Shape:
    def area(self):
        return 0 
    def perimeter(self):
        return 0 
    class Circle: 
        def __init__(self, radius):
            self.radius = radius 
        def area(self):
            a = math.pi ** 2 * self.radius 
            return a 
        def perimeter(self): 
            a1 = 2 * math.pi * self.radius 
            return a1
    class Triangle: 
        def __init__(self,t1,t2,t3):
            self.t1 = t1  
            self.t2 = t2
            self.t3 = t3
        def perimeter(self):
            b = self.t1 + self.t2 + self.t3 
            return b 
        def area(self):
             s = (self.t1 + self.t2 + self.t3)/2
             b1 = math.sqrt(s * (s - self.t1)*(s - self.t2)*(s - self.t3))
             return b1
    class Square: 
        def __init__(self, side):
            self.side = side
        def area(self):
            c = self.side**2 
            return c 
        def perimeter(self):
            c1 = 4 * self.side
            return c1 
    
    round = Circle(67)
    triangleg = Triangle(23,34,45)
    sqr = Square(123456789) 

    print("Circle - area:" , round.area(), "| perimeter:", round.perimeter() )
    print("Triangle - area:" , triangleg.area(), "| perimeter:", triangleg.perimeter() )
    print("Square - area:" , sqr.area(), "| perimeter:", sqr.perimeter() )




# the remaining part of the assigment was not understandable, sorry
