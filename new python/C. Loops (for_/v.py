"""
13. Count the number of digits in a given number.
"""
n = input("Enter your number : ")

try :
    if "." in n :
        print(f"There are {len(n)-1} digits in {n}")
    else :
        print(f"There are {len(n)} digits in {n}")
        float(n)
except ValueError:
    print("Please enter a valid number.")