"""
9. Print the multiplication table of any number.
"""
n = int(input("Enter your number : "))

print(f"Table of {n} : ")
for i in range(1,11) : 
    print(f"{n} x {i} = {n*i}")