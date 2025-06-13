"""
1234554321
1234  4321
123    321
12      21
1        1
"""
v = 1
n = int(input("Enter the length : "))
for i in range(1,n+1) :
    for a in range(1,7-i) :
        print(a,end="")
    if i == 1 :
        pass
    else :
        print(" "*v,end="")
        v += 2
    for b in range(a,0,-1):
        print(b,end="")
    print()
v = 1