"""
12. Print all prime numbers between 1 and 100.
"""
prime_found = [2]
not_found = True

for i in range(3,101):

    for prime in prime_found:

        if i % prime == 0:
            not_found = False
            break

    if not_found == True:
        prime_found.append(i)

    not_found = True

total_prime = len(prime_found)
print(prime_found)
print(f"Total Prime found in between 2 - 100 = {total_prime}")