def lone_sum(a, b, c): #Defined the function that will take 3 values at its use. (CHANGED)
    if a == b and b == c and a == c: #If all values are equal then "0" will be returned. (MOVED TO TOP OF FUNCTION)
        answer = 0
    elif a == b:  #If "a" is equal to "b" then the value of "c" is returned. (CHANGED)
        answer = c
    elif a == c: #If "a" is equal to "c" then the value of "b" will be returned.
        answer = b
    elif b == c: #If "b" is equal to "c" then the value of "a" will be returned.
        answer = a
    else: #If none of the above have been triggered, the values of "a", "b", and "c" will be added.
        answer = a + b + c
    return answer

print(lone_sum(1, 2, 3)) #Check if none are the same
print(lone_sum(7, 7, 7)) #Check if all are the same
print(lone_sum(1, 1, 3)) #Check if "a" and "b" are the same (return "c")
print(lone_sum(1, 2, 1)) #Check if "a" and "c" are the same (return "b")
print(lone_sum(1, 2, 2)) #Check if "b" and "c" are the same (return "a")
