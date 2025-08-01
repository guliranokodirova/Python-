#write a Python script that reads the students.jon JSON file and prints details of each student.
import json
students=[
              {
                "Name":"Gulirano",
                "Age":18,
                "Course": "Python_2",
                "English_level" : "C1"
              },
              {
                "Name":"Alexa",
                "Age":"24",
                "Course": "Foundation",
                "English_level" :"C2"       
              },
              {
                "Name":"Kate",
                "Age":"19",
                "Course": "Power_BI",
                "English_level" : "B2" 
              }, 
              {
                "Name":"Jenny",
                "Age"
                "":"23",
                "Course": "Python_1",
                "English_level"  : "C1"  
              }
]
with open ("students","w") as file:
 json.dump(students,file, indent = 4)
with open ("students", "r") as f:
 ucheniki = json.load(f)



for student in ucheniki:
   print(student)
#get the wether info 
import requests
api_key = "a4c011974d99974c1d1e154ad3bd8cfd"
city = "Tashkent"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
info = response.json()
print(info)
temp = info["main"]["temp"]
humid = info["main"]["humidity"]
wind_speed = info["wind"]["speed"]
print(city)
print(f"🌡️Temperature:{temp}")
print(f"💧Humidity:{humid}")
print(f"💨Wind Speed:{wind_speed}")
import json

books = [
    {
        "Name": "Pride and Prejudice",
        "Author": "Jane Austen",
        "Rating": "4.3/5"
    },
    {
        "Name": "Kite Runner",
        "Author": "Khaled Hosseini",
        "Rating": "4.4/5"
    },
    {
        "Name": "Thousand Splendid Suns",
        "Author": "Khaled Hosseini",
        "Rating": "4.4/5"
    },
    {
        "Name": "They both die in the end",
        "Author": "Adam Silvera",
        "Rating": "3.8/5"
    }
]

with open("books.json", "w") as file:
    json.dump(books, file, indent=4)

with open("books.json", "r") as file:
    books = json.load(file)

for book in books:
    if book["Name"] == "They both die in the end":
        book["Rating"] = "3.5/5"
    if book["Author"] == "Jane Austen":
        book["Author"] = "Jane Austin" 

with open("books.json", "w") as file:
    json.dump(books, file, indent=4)

print(json.dumps(books, indent=4))
