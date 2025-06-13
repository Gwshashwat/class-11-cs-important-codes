"""
15. Count the number of vowels in a string.
"""
vowels = ["a","e","i","o","u"]
total_vowels_found = 0

inp = input("Enter your string : ")

main = inp.lower()
for word in main :
    if word in vowels:
        total_vowels_found += 1

print(f"Total vowel found = {total_vowels_found}")