import math


iterations = int(input("Enter a positive integer: "))

for number in range(1, iterations + 1):
    print(f"{number}: {(1 + (1/number)) ** number}")

result = 0
for number in range(0, iterations + 1):
    result += 1/(math.factorial(number))
    print(f"{number}: {result}")