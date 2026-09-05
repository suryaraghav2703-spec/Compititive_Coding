# now lets find out power of numbers
# base case --> if power is 0 than return 1 means n == 0 than return output = 1
# Recursive relationship --> x^n = x × x^(n-1)

# now lets find power of 2 to the power 5 ( 2^5)
def power(x,n):
    if n == 0:
        return 1
    return x * power(x , n - 1)
print("power of the nubmer:", power(2,5))
