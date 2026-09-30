# Now lets find out factorial of a number
#  5!  = 5 x 4! and 4! = 4 x 3! .... and so on
#  so it means 
#  n! = n * (n-1)! -->  this is the recursvie relation 
#  now base case will be if n == 0 than return 1

#  now lets find factorial of 5
def fact(n):
    if n == 0:     # Base case
        return 1
    return n * fact(n - 1)
print("Factorial of 5:", fact(5))

