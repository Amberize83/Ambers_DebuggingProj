#There is no function defined here. based on the use of return that follows there should be a defined function that will call on those returns

if a >= b:  #If "a" is greater than or equal to "b" then the value of "c" is returned. (incorrect)
    return c
elif a == c: #If "a" is equal to "c" then the value of "b" will be returned.
    return b
elif b == c: #If "b" is equal to "c" then the value of "a" will be returned.
    return a
elif a == b and a == c and b == c: #If all values are equal then "0" will be returned.
    return 0
else: #If none of the above have been triggered, the values of "a", "b", and "c" will be added.
    return a + b + c
