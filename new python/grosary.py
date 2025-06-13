grosary = {}

while True:
    item = input("Enter your item (enter q to quit.) : ").capitalize()

    if item == "Q" :
        break 

    else :
        quantity = input("Enter the quantity of your item : ")
        grosary[item] = quantity
    
print(f"Grosary = {grosary}")