# Create a list of 20 employee IDs
employee_ids = [123456, 234567, 345678, 456789, 567890,
                678901, 789012, 890123, 901234, 123457,
                234568, 345679, 456790, 567891, 678902,
                789013, 890124, 901235, 123458, 234569]

# Create two empty lists for even and odd employee IDs
even_ids = []
odd_ids = []

# Iterate over the list of employee IDs and append them to the corresponding list
for id in employee_ids:
    if id % 2 == 0:
        even_ids.append(id)
    else:
        odd_ids.append(id)

# Print the two lists of employee IDs
print("Employees with even ID:", even_ids)
print("Employees with odd ID:", odd_ids)
