# Input marks for five courses
marks1 = int(input("Enter marks for course 1: "))
marks2 = int(input("Enter marks for course 2: "))
marks3 = int(input("Enter marks for course 3: "))
marks4 = int(input("Enter marks for course 4: "))
marks5 = int(input("Enter marks for course 5: "))

# Calculate total marks and percentage
total_marks = marks1 + marks2 + marks3 + marks4 + marks5
percentage = (total_marks / 500) * 100

# Check pass/fail and grade
if marks1 >= 40 and marks2 >= 40 and marks3 >= 40 and marks4 >= 40 and marks5 >= 40:
    if percentage >= 75:
        print("Result: Distinction")
    elif 60 <= percentage < 75:
        print("Result: First Division")
    elif 50 <= percentage < 60:
        print("Result: Second Division")
    elif 40 <= percentage < 50:
        print("Result: Third Division")
else:
    print("Result: Fail")
