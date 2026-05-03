def calculate_grade(marks):
	if any(mark < 40 for mark in marks):
		return "Fail"
	percentage = sum(marks)/len(marks)
	# print(percentage)
	if percentage>75:
		grade = "Distinction"
	elif percentage>=60:
		grade = "First Division"
	elif percentage>=50:
		grade = "Second Division"
	elif percentage>=40:
		grade = "Third Division"
	else:
		grade = "Fail"

	# print(grade)
	output = f"Aggregate Percentage: {percentage:.2f}\nGrade: {grade}"
	# return f"Aggregate Percentage: {percentage:.2f}\nGrade:{grade}"
	return output

n = int(input())
marks = map(int,input().split(" "))
marks = list(marks)
# print(marks)
print(calculate_grade(marks))
