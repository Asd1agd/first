marks = [] 
pass_count = fail_count = 0

# input marks of students
for i in range(1, 11):
    m = int(input(f"Enter marks of student {i}: "))
    marks.append(m)
    if m >= 12:
        pass_count += 1
    else:
        fail_count += 1

# calculate top scorer and lowest scorer
top_score = max(marks)
lowest_score = min(marks)

print("Top scorer:", top_score)
print("Lowest scorer:", lowest_score)
print("Total number of pass students:", pass_count)
print("Total number of fail students:", fail_count)
