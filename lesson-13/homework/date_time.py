# version 1
from datetime import datetime
from dateutil.relativedelta import relativedelta

bd = input("Please enter your birth date in format (YYYY-MM-DD): ")
birth = datetime.strptime(bd, "%Y-%m-%d")
now = datetime.now()
diff = relativedelta(now, birth)

total_months = diff.years * 12 + diff.months

total_days = (now - birth).days

print(f"You're {diff.years} years, {total_months} months, and {total_days} days old.")
# version 2 of first exercise
from datetime import datetime, timedelta 
from dateutil.relativedelta import relativedelta 

bd = input("Please enter your birth date in format (YYYY-MM-DD): ")
birth = datetime.strptime(bd, "%Y-%m-%d")
now = datetime.now()

diff = relativedelta(now, birth)

print(f"You are {diff.years} years, {diff.months} months, and {diff.days} days old.")
### Days Until Next Birthday!


bd = input("Please enter your birth date in format (YYYY-MM-DD): ")
birth = datetime.strptime(bd, "%Y-%m-%d")
now = datetime.now()
diff = relativedelta(now, birth)
this_year_bd = birth.replace(year = now.year)
if this_year_bd > now:
   upcoming_bd = this_year_bd
elif this_year_bd  < now:
   upcoming_bd = birth.replace(year = now.year + 1)
days = upcoming_bd - now


print(days) 
###Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. 
# ###Calculate and print the date and time when the meeting will end.
from datetime import datetime,date  
now = input('Enter current date and time in format: (YYYY-MM-DD HH:MM )')
duration = input('Enter duration of a scedule (HH:MM): ')
current_datetime = datetime.strptime(now, "%Y-%m-%d %H:%M")
hours, minutes  = duration.split(":")
end_time = timedelta(hours = int(hours), minutes = int(minutes))
end_of_meeting = current_datetime + end_time
print(f"Your meeting will end at {end_of_meeting}")#Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, 
# and then convert and print the date and time in another timezone of their choice.!pip install pytz
from datetime import timezone,datetime
import pytz
time = input("Please,enter date & time(YYYY-MM-DD HH:MM):")
time1 = datetime.strptime(time, "%Y-%m-%d %H:%M" )
tz_korea = pytz.timezone('Asia/Seoul')
check = datetime.now(tz_korea)
print(check)
## countdown timer
from datetime import datetime,timedelta 
now = datetime.now()
coming = now + timedelta(seconds = 100)
t1 = now.timestamp()
t2 = coming.timestamp()
while t1 <= t2:
    print("Remaining time:", datetime.fromtimestamp(t2))
    t2 = t2 -1 
# only 5  exercises were done due to lack of time 
