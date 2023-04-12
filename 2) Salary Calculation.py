# Input basic pay
basic_pay = float(input("Enter the basic pay: "))

# Calculate HRA and TA
HRA = 0.1 * basic_pay
TA = 0.05 * basic_pay

# Calculate gross salary
gross_salary = basic_pay + HRA + TA

# Calculate professional tax
professional_tax = 0.02 * gross_salary

# Calculate net salary
net_salary = gross_salary - professional_tax

# Output salary
print("Net Salary: Rs.", net_salary)
