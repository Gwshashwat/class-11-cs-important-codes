"""
5. Check whether a number is positive, negative, or zero.
"""
n = int(input("Enter your number : "))

if n > 0 :
    print(f"{n} is positive.")
elif n < 0 :
    print(f"{n} is negative.")
elif n == 0:
    print(f"{n} is 0.")
else :
    print("Something went wrong.")