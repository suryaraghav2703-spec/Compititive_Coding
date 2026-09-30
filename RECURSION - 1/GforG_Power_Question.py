#  Q.1] Given a number n, find the value of n raised to the power of its own reverse. 
# The result will always fit into a 32-bit signed integer.
# Examples:
# Input: n = 2
# Output: 4
# Explanation: The reverse of 2 is 2, and 22 = 4.
# Input: n = 10
# Output: 10
# Explanation: The reverse of 10 is 1 (leading zero is discarded), and 10 raised to the power 1 is 10.

#  so this is the question in which i have to find power but what i have to do is 
#  first create a reverse of the real and than find thei power like (real ** reverse)
n = int(input("Enter a number:"))
real = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
ans = real ** reverse
print(ans)

#  now lets dry run this code so here
#  first we made 2 variables real which is the original value and reverse which is initially zero
#  now we will start a while loop that loop will run until n becomes zero 
#  first lets take n = 123 
#  so digit = 123 % 10 which will remainder 3 
#  than reverse = 0 * 10 + 3  as reverse intially is zero and digit value just came 3 
#  so reverse will now become reverse = 3
#  than n = 123 // 10 which will give integer division which is 12. therefore n = 12
#  than again loop will run digit = 12 % 10 so digit = 2
#  than reverse = 3 * 10 + 2 which is reverse = 32 
#  reverse will remove 3 and replace it with 32 
#  than n = 12 // 10 will give n = 1 
#  than same loop and in the end when n = 0 loop ends with reverse value as  reverse = 321
#  but we have already store value of n = 123 in real named variable 
#  so ans = real ** reverse will give
#  ans = 123 ** 321  . thats our solution 