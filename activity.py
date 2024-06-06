# Write a Python script that asks the user to input a numerical score and categorizes it into grades (A, B, C, D, F) based on the following criteria:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F


# Prompt the user to enter a score
score = int(input("Enter the score (0-100): "))

# Determine the grade based on the score
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"The grade for score {score} is {grade}")