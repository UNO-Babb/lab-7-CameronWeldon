#Problem5.py
#Project Euler problem #21

from NumberTests import find_amicable_numbers

def main():
    limit = 100000
    amicables = find_amicable_numbers(limit)
    print(f"Amicable numbers under {limit}: {sorted(amicables)}")
    print(f"Sum of all amicable numbers under {limit}: {sum(amicables)}")

if __name__ == '__main__':
  main()
