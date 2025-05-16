# main.py

from NumberTests import SummationOfPrimes

def main():
    try:
        limit = int(input("Find the sum of all prime numbers below: "))
        if limit < 2:
            print("Please enter a number greater than or equal to 2.")
            return
        total = SummationOfPrimes(limit)
        print(f"The sum of all prime numbers below {limit} is {total}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()
