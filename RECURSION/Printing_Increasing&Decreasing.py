#  lets print increasing and decreasing function (simlply lets just for example print 1 to 5 and 5 to 1)

# Increasing printing 1 to 5
# Normally we'd use a loop:  
for i in range(1 ,6):
    print(i)

print()
print()
print()
#  now lets do it recursively 
# so first we want to print 1, print 2 , print 3, print 4, print 5.
# Could we say:
# "Print 1, then ask the function to print 2 to 5."

# Then:
# "Print 2, then ask the function to print 3 to 5."
# And so on. That's recursion.

#    Increasing 1 to 5
def Increasing(n):       # Create a function that accepts n
    if n == 0:      # base case
        return 
    Increasing(n - 1)
    print(n)
Increasing(5)    


print()
print()
print()

#   Decreasing 5 to 1
def Decreasing(n):
    if n == 0:   # base case
        return 
    print(n)       
    Decreasing(n - 1)
Decreasing(5)


print()
print()
print()

# Increasing to Decreasing
def num(n):
    if n == 6:
        return
    print(n)
    num(n + 1)
    print(n)
num(1)

print()
print()
print()

# Decreasing to Increasing
def decreasingIncreasing(n):
    if n == 0:
        return
    print(n)
    decreasingIncreasing(n - 1)
    print(n)
decreasingIncreasing(5)

print()
print()
print()

#  if i have to print 1 to 5 without space seprating integers like answer should be 1 2 3 4 5..... and so on 
#  so to solve this we will do 
def one_to_five(n):
    if n == 0:
        return 
    one_to_five(n - 1)
    print(n , end = " ")
one_to_five(5)        # here out put will show 1 2 3 4 5   


