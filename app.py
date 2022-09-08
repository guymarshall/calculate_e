iterations = int(input("Enter a positive integer: "))

for number in range(1, iterations + 1):
    print(f"{number}: {(1 + (1/number)) ** number}")