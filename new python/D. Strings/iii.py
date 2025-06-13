"""
16. Convert a string to uppercase without using `.upper()`.
"""
new_str = ""
inp = input("Enter your string : ")

for word in inp :
    new_str = new_str + word.capitalize()

print(f"uppercase of {inp} = {new_str}")