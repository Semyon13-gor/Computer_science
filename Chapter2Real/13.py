from datetime import datetime
current_year = datetime.now().year
a = str(input("Name"))
b = int(input("Age"))
year100 = (current_year - b) + 100
print(year100)