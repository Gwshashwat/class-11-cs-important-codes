"""
28. Count how many students scored above 90.
"""
d = {
'Shashwat': 89, 
'Gaurav': 79, 
'SB': 77, 
'Dikshant': 91, 
'Vansh': 70, 
}
total = 0

for name in d :

    value = d[name]
    if value > 90 :
        total += 1
        
print(f"{total} students scored above 90.")