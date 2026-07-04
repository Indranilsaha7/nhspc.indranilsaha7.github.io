from datetime import date # imported for more accurate current year

birth_year = int(input("Enter your birth year: "))
current_year = date.today().year
age = current_year - birth_year
print(f"Your age is {age}!")
