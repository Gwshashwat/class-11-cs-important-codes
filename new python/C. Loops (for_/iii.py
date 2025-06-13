"""
11. Write a program to find factorial of a number.
"""
n = int(input("Enter your number : "))
num = n
a = n - 1
while a != 0:
    n *= a
    a -= 1
print(f"{num}! = {n}") 