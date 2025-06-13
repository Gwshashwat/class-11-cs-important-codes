"""
23. Convert a tuple to a list and vice versa.
"""
l = [6, 6, 7, 4, 6, 0, 9, 2, 2, 3]
t = (5,6,7,4,3)

t_to_l = list(t)
l_to_t = tuple(l)

print(f"Tuple to List = {t_to_l}")
print(f"List to Tuple = {l_to_t}")