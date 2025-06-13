"""
29. Write a function to check if a number is prime.
"""
def prime(n) :
    found = True
    for i in range(1,1+n):
        
        if i % n == 0:
            found = False
        
        else:
            pass
    if found == True:
        print(f"{n} is a prime number.")
    
    else:
        print(f"{n} is not a prime number.")

n = int(input("Enter your number : "))

prime(n)