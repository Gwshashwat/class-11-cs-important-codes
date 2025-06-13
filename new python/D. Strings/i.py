"""
14. Check if a string is a palindrome.
"""
n = input("Enter your string : ")

start_part = []
end_part = []
start_run = 0
end_run = 0

if len(n) % 2 == 0:
    for start_word in n :
        if start_run == len(n)/2 :
            break
        else :
            start_part.append(start_word)
            start_run += 1

    
    for end_word in n :
        if end_run == len(n)/2 :

            end_part.append(end_word) 
        else :
            end_run += 1 

    end_part.reverse()
    if start_part == end_part :
        print("string is a palindrome.")

    else :
        print("string is not a palindrome.")

else :
    for start_word in n :
        if start_run == (len(n)-1)/2 :
            break
        else :
            start_part.append(start_word)
            start_run += 1

    
    for end_word in n :
        if end_run == (len(n)+1)/2 :

            end_part.append(end_word) 
        else :
            end_run += 1 

    end_part.reverse()
    if start_part == end_part :
        print("string is a palindrome.")

    else :
        print("string is not a palindrome.")

print(start_run)
print(end_run)
# MADDEEEE BYYY MEEEE SHASHWAT