##all the 4 exercises in one code
import pyodbc
connection_string = pyodbc.connect( 
                               'DRIVER={SQL Server};'
                               'Server=WIN-U0KI34USBPL;'
                               'Database=Python;'
                               'trusted_Connection=yes;'
                               )
print('Connected Successfully')
cursor = connection_string.cursor()
create_table = '''drop table if exists Roster create table dbo.Roster(Name varchar(30), Species varchar(30), age int)'''
insert_table = '''insert into dbo.Roster (Name, Species, age) 
                  values ('Benjamin Sisko','Human',  40),
                  ('Jadzia Dax','Trill',300),
                  ('Kira Nerys','Bajoran',29)'''
update_table = ''' update dbo.Roster
                   set Name = 'Ezri Dax'
                   where Name = 'Jadzia Dax' '''
select_statement = ''' select Name, age from Roster
                       where Species = 'Bajoran' '''
cursor.execute(create_table)
cursor.execute(insert_table)
cursor.execute(update_table)
cursor.execute(select_statement)
rows = cursor.fetchall()

for row in rows:
    print(f"Name: {row[0]}, Age: {row[1]}")

cursor.commit()
cursor.close()
connection_string.close()
