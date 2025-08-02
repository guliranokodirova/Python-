import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}
# 1 (student grade)
df1 = pd.DataFrame(data1)
df1['Average'] = df1[['Math','English','Science']].mean(axis=1)
df1
#2 (student grade)
sort = df1.sort_values('Average', ascending = False)
sort.head(1)
#3 (student grade)
df1['Total'] = df1['Math'] + df1['English'] + df1['Science']
df1 
# 4 (student grade) bar chart  
import pandas as pd
from matplotlib import pyplot as plt 

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
avg_math = df1['Math'].mean()
avg_eng = df1['English'].mean()
avg_science = df1['Science'].mean()

subjects = ['Math', 'English', 'Science']
averages = [avg_math, avg_eng, avg_science]
colors = ['pink', 'skyblue', 'yellow']

plt.bar(subjects, averages, color = colors, width = 0.3)

plt.title("Average Grades Per Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Score")
plt.show()
# 1 (Sales Data)
import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
ts = df2[['Product_A','Product_B','Product_C']].sum(axis=0)
ts
# 2 (sales data)
df2['Total'] = df2[['Product_A','Product_B','Product_C']].sum(axis=1)
top_sales = df2['Total'].max()
top_dates = df2[df2['Total'] == top_sales]
top_dates
# 3 (sales data)
df2['A_percentage_change'] = df2['Product_A'].pct_change()*100
df2['B_percentage_change'] = df2['Product_B'].pct_change()*100
df2['C_percentage_change'] = df2['Product_C'].pct_change()*100
df2
# 4 (sales data) line chart 
import pandas as pd
import matplotlib.pyplot as plt


data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)


plt.figure(figsize=(10, 6))
plt.plot(df2['Date'], df2['Product_A'], label="Product A", marker='o')
plt.plot(df2['Date'], df2['Product_B'], label="Product B", marker='*')
plt.plot(df2['Date'], df2['Product_C'], label="Product C", marker='x')

plt.title("Sales Trends for Each Product Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
# 1 (employee info)
import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)
avg_per_department = df3.groupby('Department')['Salary'].mean()
print(avg_per_department)
# 2 (employee info) 
sorted_experience = df3.sort_values('Experience (Years)', ascending = False)
sorted_experience.head(1)
# 3 (employee info)
min_salary = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary) * 100
print(df3[['Name', 'Salary', 'Salary Increase']])
# 4 (employee info) bar chart 
from matplotlib import pyplot as plt 
num = df3.groupby("Department")["Employee_ID"].count()

colors = ['navy', 'grey', 'green', 'black']
plt.bar(num.index, num.values, color = colors, width = 0.4)
plt.title("Number of Employees inEach Department")
plt.xlabel("Departments")
plt.ylabel("Employee Numbers")
plt.show
# 1 ( customer order)
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
revenue = df4['Total_Price'].sum()
print('Total revenue from all sales:', revenue)
# 2 (Customer orders) 
max = df4['Quantity'].max()
print(max)
# 3 (Customer orders)
avg = df4['Quantity'].mean()
print(avg)
# 4 (Costomer orders) -- pie chart
from matplotlib import pyplot as plt
df4 
units_sold = df4.groupby('Product')['Quantity'].sum()
plt.pie(units_sold, labels = units_sold.index, startangle = 90)
plt.title("Distribution of sales across different products")
plt.axis('equal')
plt.show()
