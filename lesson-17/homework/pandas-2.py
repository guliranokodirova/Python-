import pandas as pd
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
     'Age': [25, 30, 35, 40],
      'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
      } 
df = pd.DataFrame(data)

#Rename column names using function. "First Name" --> "first_name", "Age" --> "age
def rename(col):
    return col.lower().replace(' ','_')
df = df.rename(columns=lambda x: rename(x))
print(df)                                                                                                                                                                   #Find the mean age of the individuals
mean_age = df['age'].mean()
print('mean age:', mean_age)                                                                                                                              #Select and print only the 'Name' and 'City' columns
df = df[['first_name','city']]
df                                                                                                                                                                     # add new salary column with random values
import numpy as np
import pandas as pd
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
     'Age': [25, 30, 35, 40],
      'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
      } 
df = pd.DataFrame(data) 
df['salary'] = np.random.randint(low = 200, high = 1000, size=len(df))
df
## summary: to get a random value always use numpy                                                                                ## Display summary statistics of the DataFrame
df.describe()                                                                                                                                                      import pandas as pd 
data = {
    'Month':['Jan','Feb','Mar','Apr'],
    'Sales':[5000,6000,7500,8000],
    'Expenses':[3000,3500,4000,4500]
}
df = pd.DataFrame(data)
max_sales = df['Sales'].max()
max_expenses = df['Expenses'].max()

min_sales = df['Sales'].min()
min_expenses = df['Expenses'].min()

avg_sales = df['Sales'].mean()
avg_expenses = df['Expenses'].mean()

print('Maximum value of sales:', max_sales)
print('Maximum value of expenses:', max_expenses)
print('Minimum value of sales:', min_sales)
print('Minimum value of expenses:', min_expenses)
print('Average value of sales:', avg_sales)
print('Average value of expenses:', avg_expenses)                                                                    import pandas as pd 
data = {
    'Category':['Rent','Utilities','Groceries','Entertainment'],
    'January':[1200,200,300,150],
    'February':[1300,220,320,160],
    'March':[1400,240,330,170],
    'April':[1500,250,350,180]
}
df = pd.DataFrame(data)
df.set_index('Category', inplace=True)
max_expenses = df.max(axis=1)
min_expenses = df.min(axis=1)
avg_expenses = df.mean(axis=1)
print('Maximum expenses for each category:')
print(max_expenses)
print('Minimum expenses for each category:')
print(min_expenses)
print('Average expenses for each category:')
print(avg_expenses)
