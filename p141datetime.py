import datetime
today = datetime.date.today()
birthDate = datetime.date(2005, 1, 29)
age = today.year - birthDate.year
print(age)
