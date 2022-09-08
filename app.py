import math
from decimal import Decimal, getcontext


def main():
    getcontext().prec = 100
    
    iterations = int(input("Enter a positive integer: "))

    results = []
    for number in range(1, iterations + 1):
        results.append(f"{number}: {(Decimal(1) + (Decimal(1)/Decimal(number))) ** Decimal(number)}\n")
    
    print("Writing to file...")
    
    with open("output.txt", "w") as file:
        for result in results:
            file.write(result)
    
    print("File write complete.")

if __name__ == "__main__":
    main()
