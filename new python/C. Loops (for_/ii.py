"""
10. Print the sum of the first `n` natural numbers.
"""
n = int(input("Enter your number : "))
a = n
for i in range(1,n): 
    n += i

print(f"The sum of first {a} natural numbers = {n}")