# import the required package
from datetime import datetime
def calculate_age(birthdate):
	today = datetime.now()
	birthdate = datetime.strptime(birthdate,"%d-%m-%Y")
	return today.year - birthdate.year - ((today.month,today.day)<(birthdate.month,birthdate.day))
def convert_salary_to_dollars(salary_in_rupees):
	conversion_rate=83.33333
	return salary_in_rupees/conversion_rate
	

birthdate = input()
salary_in_rupees = float(input())
age = calculate_age(birthdate)
salary_in_dollars = convert_salary_to_dollars(salary_in_rupees)
print(f"Age: {age}")
print(f"Salary in dollars: {salary_in_dollars:.2f}")
