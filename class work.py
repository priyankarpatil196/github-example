
import datetime
x=datetime.datetime.now()
print(x)


x=datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

x=datetime.datetime(2020,5,17)
print(x)

x=datetime.datetime.now()
print(x.year)
print(x.strftime("%B"))


x=datetime.datetime(2020,5,30)
print(x.strftime("%A"))

from datetime import timedelta
from datetime import datetime
print("today is:"+str(datetime.now()))
print("one year from now it will be:"+str(datetime.now()+timedelta(days=365)))
print("in one week and 4 days it will be"+str(datetime.now()+timedelta(weeks=1,days=4)))

t=timedelta(hours=1)
print("total seconds=",t.total_seconds())
t=timedelta(hours=24)
print("total seconds=",t.total_seconds())
t=timedelta(days=10)
print("total seconds=",t.total_seconds())

import calendar
cal=calendar.month(2019,9)
print("here is calendar:")
print(cal)

import random
print(random.randint(1,10))
for x in range(20):
    print(random.randint(1,101))

val=input("enter value")
print(val)









      
