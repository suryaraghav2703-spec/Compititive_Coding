# return "" --> Base case
#  reversing a string using recursion
def reverseString(s):
    if s == "":
        return ""
    return reverseString(s[1:]) + s[0]
print("Reverse of this String:" , reverseString("Hello"))

#  using Two Pointer
h = "DANNY"
arr = list(h)
left = 0
right = len(arr) - 1
while left < right:
    arr[left] , arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print( "Reverse of String: ", "".join(arr))  

#  using for loops
j = "Hello"
reverse = ""
for i in range(len(j)-1, -1, -1):
    reverse += j[i]
print("Reverse of this String: ", reverse)    
