"""
8. Write a program to calculate the electricity bill:
 - Rs.5 per unit for the first 100 units
 - Rs.8 per unit for units above 100
 """
units = int(input("Enter the units consumed : "))
if units <= 100 :
    print(f"the electricity bill = Rs.{units*5}")

else :
    print(f"the electricity bill = Rs.{((units - 100)*8) + 500}")