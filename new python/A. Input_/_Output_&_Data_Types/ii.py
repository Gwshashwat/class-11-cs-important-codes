"""
2. Write a program to find the average of 3 numbers entered by the user.
"""
a = float(input("Enter the first number : "))
b = float(input("Enter  the second number : "))
c = float(input("Enter the third number : "))
avg = (a+b+c)/2
print(f"Avarage = {avg.__round__(2)}")