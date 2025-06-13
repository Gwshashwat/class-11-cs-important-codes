"""
24. Check whether an element exists in a tuple or not
"""
total = 0 

t = ("list",5,True,False)

for item in t :
    total += 1

if total == 0:
    print("Tuple is empty.")
else:
    print(f"Tuple is not empty, it has {total} elements.")