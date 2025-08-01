## homework 2 
import pandas as pd
df = pd.read_csv(r'C:\Users\user\Downloads\tackoverflow_qa.csv')
df = df.head()
##Find all questions that were created before 2014
df['creationdate'] = pd.to_datetime(df['creationdate'])
df['Year'] = df['creationdate'].dt.year
# filter 
df = df.loc[df['Year']<2014]
df
## score higher than 50 
df = df.loc[df['score']> 50]
df
#Find all questions with a score between 50 and 100
import pandas as pd
df = pd.read_csv(r'C:\Users\user\Downloads\tackoverflow_qa.csv')
df = df.head()
df = df.loc[df['score'].between(50,100)]
df
#Find all questions answered by Scott Boston
import pandas as pd
df = pd.read_csv(r'C:\Users\user\Downloads\tackoverflow_qa.csv')
df
df = df.loc[df['ans_name'] == 'Scott Boston']
df
# answered by the following 5 users
df = pd.read_csv(r'C:\Users\user\Downloads\tackoverflow_qa.csv')
df = df.loc[df['answercount'] == 5]
df
##Find all questions that were created between March, 2014 and October 2014
#  that were answered by Unutbu and have score less than 5
df = pd.read_csv(r'C:\Users\user\Downloads\tackoverflow_qa.csv')
df['creationdate'] = pd.to_datetime(df['creationdate'])
start = '2014-03-01'
end = '2014-10-31'
df = df.loc[
    (df['creationdate'].between(start,end)) & 
    (df['ans_name'] == 'Unutbu') & 
    (df['score'] < 5)
]
df 
##Find all questions that have score between 5 and 10 or
#  have a view count of greater than 10,000
df = pd.read_csv(r'C:\Users\user\Downloads\tackoverflow_qa.csv')
df = df.loc[df['score'].between(5,10) | (df['viewcount'] > 10000)]
df
df = pd.read_csv(r'C:\Users\user\Downloads\tackoverflow_qa.csv')
df
df = df.loc[df['ans_name'] != 'Scott Boston']
df
#1
titanic_df = pd.read_csv(r"C:\Users\user\Downloads\titanic.csv")
titanic_df.head()
t_df = titanic_df.loc[
    (titanic_df['Pclass']==1) &
    (titanic_df['Sex'] =='female') & 
    (titanic_df['Age'].between(20,30))]
t_df
#2 
titanic_df = pd.read_csv(r"C:\Users\user\Downloads\titanic.csv")
titanic_df.head()
new_df = titanic_df.loc[titanic_df['Fare'] > 100]
new_df.head()
# 3
titanic_df = pd.read_csv(r"C:\Users\user\Downloads\titanic.csv")
titanic_df.head()
alone_passenger_df = titanic_df.loc[
    (titanic_df['Survived'] == 1) & 
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0) ]
alone_passenger_df.head()
# 4 
titanic_df = pd.read_csv(r"C:\Users\user\Downloads\titanic.csv")
titanic_df.head()
c_passenger_df = titanic_df.loc[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50 )]
c_passenger_df.head()
#5 
titanic_df = pd.read_csv(r"C:\Users\user\Downloads\titanic.csv")
titanic_df.head()
PS_SP_df  = titanic_df.loc[
    (titanic_df['SibSp'] > 1) & 
    (titanic_df['Parch'] > 1 )]
PS_SP_df.head()
#6 
titanic_df = pd.read_csv(r"C:\Users\user\Downloads\titanic.csv")
titanic_df.head()
early_death_df = titanic_df.loc[
    (titanic_df['Age'] <=15) &
    (titanic_df['Survived'] == 0)]
early_death_df.head()
# 7
titanic_df = pd.read_csv(r"C:\Users\user\Downloads\titanic.csv")
titanic_df.head()
cabin_df = titanic_df.loc[
    (titanic_df['Cabin'] != 'NaN') & 
    (titanic_df['Fare'] > 200 )]
cabin_df.head()
# 8 
titanic_df = pd.read_csv(r"C:\Users\user\Downloads\titanic.csv")
titanic_df.head()
odd_pass_id_df = titanic_df.loc[(titanic_df['PassengerId'] % 2 != 0 )]
odd_pass_id_df.head()
# 9 
titanic_df = pd.read_csv(r"C:\Users\user\Downloads\titanic.csv")
titanic_df.head()
# Count the occurrences of each ticket number
ticket_counts = titanic_df['Ticket'].value_counts()

# Filter for ticket numbers that appear exactly once
unique_ticket_numbers = ticket_counts[ticket_counts == 1].index

# Extract the rows where the ticket number is in the list of unique ticket numbers
unique_tick_pass_df = titanic_df[titanic_df['Ticket'].isin(unique_ticket_numbers)]

# Display the resulting DataFrame
unique_tick_pass_df.head()
# 10 
titanic_df = pd.read_csv(r"C:\Users\user\Downloads\titanic.csv")
titanic_df.head()
miss_df = titanic_df.loc[(titanic_df['Name'].str.contains('Miss')) & (titanic_df['Pclass'] == 1)]
miss_df.head()
