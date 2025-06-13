"""
32. Write a function that returns the reverse of a string.
"""
string = input("Enter your string : ")

l = list(string)

l.reverse()

new = ""

for word in l:
    new += word

print(new)