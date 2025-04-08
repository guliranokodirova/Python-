#Create a list containing five different fruits and print the third fruit.
ls = ['banana','apple','kiwi','orange','mango']
print(ls[2])

#Create two lists of numbers and concatenate them into a single list.
ls1 = [1,2,3,4,5]
ls2 = [11,12,13,14,15]
print(ls1 + ls2)

my_list = [1,2,3,4,5,6]
first = my_list[0]
#middle = 
last = my_list[-1]

#Create a list of your five favorite movies and convert it into a tuple.
movie = ('Interstellar','Titanik','The Notebook','Blue Lagoon','Openheimer')
print(movie)

#Given a list of cities, check if "Paris" is in the list and print the result.
city = ['Tashkent','Rio De Janeiro','Paris']
check = 'Paris'
if check in city:
 print(f"Yes, it is in list")
else:
 print(f"Not identified")

#Create a list of numbers and duplicate it without using loops.
num = [1,2,3,4,5,6]
print(num * 2)

#Given a list of numbers, swap the first and last elements.
num = [1,2,3,4,5,6]
num[0], num[-1] = num[-1], num[0]
print(num)

#Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
my_tuple =(1,2,3,4,5,6,7,8,9,10)
my_tuple[2:6:1]

#Create a list of colors and count how many times "blue" appears in the list.
pallet = ['Pink','Blue','Yellow','Blue','Blue','Red']
pallet.count('Blue')

#Given a tuple of animals, find the index of "lion".
animals = ('lion','sparrow','fish','bird')
animals.index('lion')

#Create two tuples of numbers and merge them into a single tuple.
t1 = (1,2,3,4)
t2 = (5,6,7,8)
t12 = t1 + t2 
print(t12)


#Given a list and a tuple, find and print their lengths.
list1 = [1,2,34,5]
tuple = (1,2,3,4,5,6,7,90,34)
a = len(list1)
b = len(tuple)
print(f"Lengths of the list and the tuple are {a} and {b} respectively")

#Create a tuple of five numbers and convert it into a list.
my_tuple = (1,2,3,4,5)
a = list(my_tuple)
print(a)

#Given a tuple of numbers, find and print the maximum and minimum values.
t1 = (12,34,78,45)
a = max(t1)
b = min(t1)
print(f'Max value within a tuple is {a} and min value within a tuple is {b}')

#reverse the tuple
t1 = (12,34,78,45)
print(t1[::-1])
