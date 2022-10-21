from datetime import datetime
from datetime import date
k=datetime.date (datetime.now())
# print(k)
today=date.today()
# print(today)
year=today.year
# print(year)
month=today.month
# print(month)
day=today.day
# print(day)
print("WELCOME TO AGE CALCULATOR")
name=input("enter your name:-")
x=int(input("Enter the year you born:-"))
y=int(input("Enter the month you born:-"))
z=int(input("Enter the date you born:-"))
#birthdate=date(int(x.get()),(int(y.get()),(int(z.get()),
        
age=year-x-((month,day)<(y,z))
print()
print(name,"yours age is",age)


