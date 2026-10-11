# Given an array, find an index where:
# Sum of elements on the left = Sum of elements on the right
# The pivot index itself is not included in either sum.

# EXAMPLE:
# arr = [ 1, 7, 3, 6, 5, 6]
# Here at index 3 element is 6.
# So on left side of the pivot element 1 + 7 + 3 = 11
# On right side of the pivot element 5 + 6 = 11
# Therefore the answer is 3.

# Step 1: Understand the logic
# The straightforward approach is:
# For every index:
# 1.) Calculate the sum of the left side
# 2.) Calculate the sum of the right side.
# 3.) Compare both sums.
# 4.) If they are equal, return that index.

# But calculating sums repeatedly is inefficient.

# Instead, we can use the total sum.
# Suppose:
# total_sum = sum of the complete array
# left_sum = sum of elements before current index
# For the current element arr[i]:
# right_sum = total_sum - left_sum - arr[i]
# Why?
# Because:
# total_sum = left_sum + arr[i] + right_sum
# Therefore:
# right_sum = total_sum - left_sum - arr[i]

# PSEUDOCODE: 
# Find total sum of the array 
# set left_sum = 0
# for every index i:
#     right_sum = total_sum - arr[i] - left_sum 
#     if left_sum == right_sum:
#        return i
#     add arr[i] to left_sum
# return -1

# DRY RUN: 
# arr = [ 1, 7, 3, 6, 5, 6]
# total_sum = 1 + 7 + 3 + 6 + 5 + 6 = 28
# Inititally left_sum = 0
# Index     Element     Left sum    Right sum     Pivot?
#  0           1            0          27           NO
#  1           7            1          20           NO
#  2           3            8          17           NO
#  3           6           11          11           YES
#  HENCE:--- at index 3 , element 6 is the pivot point where left and right sum are equal which is 11.

def pivotIndex(arr):
    total_sum = 0
    for i in arr:
        total_sum += i
    left_sum = 0
    for i in range(len(arr)):
        right_sum = total_sum - arr[i] - left_sum
        if left_sum == right_sum:
            return i
        left_sum += arr[i]
    return -1
arr = [1, 3, 7, 6, 5, 6]
answer = pivotIndex(arr)
print("Pivot Index: ", answer)    
