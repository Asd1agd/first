import random

# Generate a random 5-digit number with the first digit not 0
num = random.randint(10000, 99999)
while num % 10 == 0:
    num = random.randint(10000, 99999)

# Check if the number and its reverse are the same
if str(num) == str(num)[::-1]:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
