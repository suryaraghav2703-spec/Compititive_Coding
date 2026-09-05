#  Sum of Array
#  using recursion   taking indexing 
def sum_array(arr, index):
    if index == len(arr):
        return 0
    return arr[index] + sum_array(arr, index + 1)
arr = [2,4,6,8,10]
print("Sum of Array: ", sum_array(arr, 0))

#  using recursion but taking element
def sumArr(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + sumArr(arr, n - 1)
arr = [2,4,6,8,10]
print("sum of Array: ", sumArr(arr, 5)) 

# using loops
def sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total
arr = [2,4,6,8,10]
print("Sum of Array: " , sum(arr))    