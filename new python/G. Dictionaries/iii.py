"""
27. Delete a student record from the dictionary by name.
"""
d = {
'Shashwat': 89, 
'Gaurav': 79, 
'SB': 77, 
'Dikshant': 70, 
'Vansh': 70, 
}

new_d = {}

a = input("Enter the name of student you want to remove : ").capitalize()

for name in d :

    if name == a :
        pass
    else:
        value = d[name]
        new_d[name] = value

print(new_d)