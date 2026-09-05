#  lets count digits 
#  if n == 0 return 0 --> Base case
# n // 10 --> recursive Case 
# it will reduce one digit from the end 
def countdigits(n):
    if n == 0:
        return 0 
    return 1 + countdigits(n // 10)
print("Digit Count: " , countdigits(12345))

# using loops  
k = 12345
count = 0
if k == 0:
    count = 1   
else:
    while k != 0:
        k = k // 10
        count += 1
print("Number of Digits:", count)   

# sum  of digits using loops
num = 12345
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10
print("Sum of Digits: ", sum)    


#  sum of digits using recursion
def sum_digits(num):
    if num == 0:
        return 0
    return (num % 10) + sum_digits(num // 10)
print("sum of Digits: ", sum_digits(12345))
