import math
from decimal import Decimal, getcontext


def main():
    getcontext().prec = 100
    
    iterations = int(input("Enter a positive integer: "))

    results = []
    for number in range(1, iterations + 1):
        # print(f"{number}: {(1 + (1/number)) ** number}")
        results.append(f"{number}: {(Decimal(1) + (Decimal(1)/Decimal(number))) ** Decimal(number)}\n")
    
    with open("output.txt", "w") as file:
        for result in results:
            file.write(result)

if __name__ == "__main__":
    main()
