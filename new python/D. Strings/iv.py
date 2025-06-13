"""
17. Write a program to count how many times a character appears in a string.
"""
d = {}

inp = input("Enter your string : ").upper()

for char in inp :
    if char in d :
        d[char] += 1

    else :
        d[char] = 1
        
print(d)