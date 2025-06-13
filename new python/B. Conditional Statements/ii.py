"""
6. Check whether a number is divisible by 2 and 3
"""
n = int(input("Enter your number : "))
if n % 2 == 0 and n % 3 == 0 :
    print(f"{n} is divisible by both 2 and 3.")
elif n % 2 == 0:
    print(f"{n} is only divisible by 2.")
elif n % 3 == 0:
    print(f"{n} is only divisible by 3.")
else :
    print(f"{n} is neither divisible by 2 nor 3.")