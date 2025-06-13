"""
26. Update the marks of a student in the dictionary.
"""
d = {
'Shashwat': 89, 
'Gaurav': 79, 
'SB': 77, 
'Dikshant': 70, 
'Vansh': 70, 
}
a = input("Enter the name of student : ").capitalize()
if a in d:
    b = input(f"Enter the revised marks of {a} : ")
    d[a] = b
    print(d)

else : 
    print(f"There is not any student named {a}.")