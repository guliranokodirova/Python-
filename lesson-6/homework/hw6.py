#2 from 0 to n, find **2
n = int(input("Enter max number: "))
numbers = list(range(n))

for i in numbers:
    print(i**2)

#3.1  Print first 10 natural numbers using a while loop 

cnt = 1
while cnt < 11: 
    print(cnt, end = ' ')
    cnt = cnt + 1


# 3.2 Print the pattern up to 5
n = int(input("Enter height of your tree: "))
for i in range(1,n + 1):
   for j in range(1,i + 1):
      print(j, end = " ")
   print()


# 3.3  Calculate sum of all numbers from 1 to a given number 
n = int(input("Enter max value: "))
sum = 0

for i in range(1, n + 1):
    sum += i 

print(sum)



# 4  Print multiplication table of a given number  
n = int(input("Enter number: "))
for i in range(1,10):
    print(f'{n} x  {i} = {n*i}')


# 5 Display numbers using a loop 
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
     if i == 75:
        print(i)
     elif i == 150:
         print(i)
     elif i == 145: 
         print(i)




# 6   Count the total number of digits in a number 
n = int(input("Enter number: "))
cnt_length = len(str(n))
print(cnt_length)
      



#7 Print reverse number tree pattern
n = int(input("Enter the height of your tree: "))
for i in range(n-1, 0, -1):
   for j in range(1,i + 1):
      print(j, end = " ")
   print()


   #8 reversed list / loop 
list1 = [10, 20, 30, 40, 50] 
for i in list1:
     a = reversed(list1)
     print(a)


    #9 
for i in range(-10, 0):
       print(i)


       #10
for i in range(5):
    print(i)

print("Done")


11#
start = int(input(" "))
end = int(input(" "))

for num in range(start, end + 1):
    if num > 1:  
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)  


#4
def uncommon_elements(list1, list2):
    result = []

    l1 = list1[:]
    l2 = list2[:]


    for item in l1:
        if item in l2:
            l2.remove(item)  
        else:
            result.append(item)

    result.extend(l2)

    return result
