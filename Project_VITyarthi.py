from datetime import date

def calculate_age(birth_date):
   today = date.today()
   age_years = today.year - birth_date.year
   age_months = today.month - birth_date.month
   age_days = today.day - birth_date.day
   
   if age_days < 0:
       age_months -= 1
       age_days += (date(today.year, today.month, 1) - date(today.year, today.month - 1, 1)).days

   if age_months < 0:
       age_years -= 1
       age_months += 12
   return age_years, age_months, age_days

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))
birth_date = date(birth_year, birth_month, birth_day)
age_years, age_months, age_days = calculate_age(birth_date)

print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")