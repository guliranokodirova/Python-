#lesson4


#Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict = {'apple':10,'orange':4,'banana':6}
sorted(my_dict)
sorted(my_dict, reverse=True)


#add a key to dict 
my_dict = {0: 10, 1: 20}
my_dict[2] = 30


 #add uo three dictionaries 
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
print(my_dict) 


#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
dicty = {0:1,1:2,2:3,3:4,4:5}
for key in dicty: 
 dicty[key]= dicty[key]**2 
 
 
 
 #Write a Python script to print a dictionary where the keys
#  are numbers between 1 and 15 (both included) and the values are the square of the keys.
onetofive = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,13:13,14:14,15:15}
for key in onetofive: 
 onetofive[key]= onetofive[key]**2
print(onetofive)
print(dicty)



#set

  #Write a Python program to create a set.
my_set = {1,2,3}
print(my_set)  


#Write a Python program to iterate over sets.
sety = {1,2,3,4,5,6,7,8,9,10}
for i in sety:
 print(i)


 #Write a Python program to add member(s) to a set.
sety = {1,2,3,4,5}
sety.add(6)
print(sety) 


 #Write a Python program to remove item(s) from a given set.
sety = {1,2,3,4,5}
sety.remove(2)
print(sety)

 #Remove an element if its given
sety = {1,2,3,4,5}
sety.discard(6)
print(sety)
