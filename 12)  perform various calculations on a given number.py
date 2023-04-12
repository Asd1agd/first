import math

# Accept the number
num = int(input("Enter a number: "))

# Square root of number
sqrt = math.sqrt(num)
print("Square root of", num, "is", sqrt)

# Square of number
square = num ** 2
print("Square of", num, "is", square)

# Cube of number
cube = num ** 3
print("Cube of", num, "is", cube)

# Check for prime
is_prime = True
for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# Factorial of number
factorial = 1
for i in range(2, num+1):
    factorial *= i
print("Factorial of", num, "is", factorial)

# Prime factors
factors = []
divisor = 2
while divisor <= num:
    if num % divisor == 0:
        factors.append(divisor)
        num //= divisor
    else:
        divisor += 1
print("Prime factors of", num, "are", factors)
