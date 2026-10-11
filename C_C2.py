#                                  SESSION-1 

#                             LEVEL 1 (FOUNDATION):

# Q.1] find max element in an array
arr = 2,7,8,14,13,9
max_element = arr[0]
for i in arr:
    if i > max_element:
        max_element = i
print("Maximun Element: ", max_element)     

# Q.2] find min element in an array
arr = 2,7,8,14,13,9
min_element = arr[0]
for i in range (len(arr)):
    if arr[i] < min_element:
        min_element = arr[i]
print("Minimun Element: ", min_element) 

# Q.3] sum of arrays
x = [2,4,6,8]
sum = 0
for i in range(len(x)):
    sum += x[i]
print("Sum of Arrays: " ,sum)   

# Q.4] Count Even Numbers
c = [2,5,8,9,10,13,19]
count = 0
for i in c:
    if i % 2 == 0:     # for odd count just write != 
        count += 1
print("Even Count is: ",count)     

# Q.5] Reverse an Array
# M-1 (loops)
r = [1,2,3,4,5]
reverse = []
for i in range(len(r)-1, -1, -1):   # range function has three values range(Start , Stop , Step)
    reverse.append(r[i])
print("Reverse Array:", reverse)  

# M-2 (Two Pointer Approach) best 
array = [1,2,3,4,5]
left = 0
right = len(array) - 1
while left < right:
    array[left],array[right] = array[right], array[left]
    left += 1
    right -= 1
print("Reverse of this array:", array)     




#                           LEVEL 2 (LOGIC BUILDING):
# Q.6] Second Largest
s= [5, 10, 8, 20, 3]
max1 = s[0]
max2 = s[0]
for i in s:
    if i > max1:
        max2 = max1
        max1 = i
    elif i > max2 and i != max1:
        max2 = i
print("Second Max: " ,max2)

# Q.7] Count Occurrences
o =[2,4,2,7,2,9]
target = 2
count = 0
for i in o:
    if i == target:
        count += 1
print("Number of Occurance is: ",count)  

# Q.8] Find Duplicate
# M-1 by looops brute force not optimal   T.C = n^2
d= [1,3,4,2,2]
for i in range(len(d)):
    for j in range(i + 1, len(d)):
        if d[i] == d[j]:
            print("Duplicate Element is:" , d[i])

# M-2 using set
D = [1,3,4,2,2]
set = set()
for i in d:
    if i in set:
        print("Duplicate element is:", i)
        break
    set.add(i)              


# Q.8] find the subarray with the largest sum, and return its sum.
nums = [-2,1,-3,4,-1,2,1,-5,4]      # output = 6
max_sum = nums[0]
current_sum = nums[0]
for i in range (1, len(nums)):
    if nums[i] > current_sum + nums[i]:
        current_sum = nums[i]

    else:
        current_sum += nums[i]

    if current_sum > max_sum:
        max_sum = current_sum
print("MAX SUBARRAY: ",max_sum)        


# Q.9] #  we need to check and return if target element is present in the sorted array if yes than return on 
# which index otherwise return number greater than the target element
ary = [2,3,5,7,9,14,17]
target = 10
# first lets solve using loops T.C = o(n)
for i in range(len(ary)):
    if (ary[i] >= target):
        print(i)
        break  

# best approach binary search T.C = o(log n)
low = 0
high = len(ary) - 1
ans = -1
while low <= high:
    mid = (low + high) // 2
    if ary[mid] >= target:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1
print(ans)        


# find target in 2-D array
matrix = [
    [1,4,5,7],
    [8,9,12,14],
    [17,19,20,21],
    [28,36,44,50]
]
target = 20
got = 0
found = False
for i in matrix:
    for j in i:
        if j == target:
            got += j
            found = True
            break
if found == True:  
    print("Target Found:", got) 
else:
    print("Not Found")                              
    
# transpose of a matrix
matrix = [
    [1,4,5,7],
    [8,9,12,14],
    [17,19,20,21],
    [28,36,44,50]
]
for i in range(len(matrix)):
    for j in range(i + 1, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print(matrix)

print()
print()

# sorted 2-D array
matrix = [
    [2,7,1,3],
    [8,4,12,6],
    [14,5,26,19]
]
arr = []
for i in matrix:
    for j in i:
        arr.append(j)
arr.sort()
k = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j] == arr[j]
        k += 1
print(matrix)    

print()
print()
# Rotate matrix by 90 degree
matrix = [
    [1,2,3,4],
    [12,15,20,30],
    [26,34,24,21],
    [36,41,32,48]
]

for i in range(len(matrix)):
    for j in range(i +1, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

for i in range(len(matrix)):
    left = 0
    right = len(matrix) - 1
    while left < right:
        matrix[i][left],matrix[i][right] = matrix[i][right], matrix[i][left]
        left += 1
        right -= 1
print("90 degree rotated:",matrix)

# leetcode - 881(boats to save people)
people = [3,3,4,5]
limit = 5




# leetcode - 1394 (lucky integer in an array)


# PATTERN PRINTING 
# *        *
# **      **
# ***    ***
# **********

n = 4
for i in range(1,n+1):
    print("*" * i + " " *(2*(n-i))  + "*"* i , end = " ")
    print()

print()
print()

# *
# **
# ***
# ****
# *****
n = 5
for i in range(1,n+1):
    print("*"*i, end = " ")
    print()

print()
print()    

# *****
# ****
# ***
# **
# *
n = 5
for i in range(1,n+1):
    print("*" * (n + 1 - i), end = " ")
    print()

print()
print()

# *****
# *****
# *****
# *****
# *****
n = 5
for i in range(1, n + 1):
    print("*" * n, end = " ")
    print()

print()
print()

# Given an integer array arr[], which denotes the positions of stalls. All the positions are distinct. 
# There are k aggressive cows.
# Assign the cows to the stalls such that the minimum distance between any two cows is maximized.

stalls = [1, 2, 4, 8, 9]
k = 3
stalls.sort()
low = 1
high = stalls[-1] - stalls[0]
answer = 0
while low <= high:
    mid = (low + high) // 2
    cows = 1
    last_position = stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= mid:
            cows += 1
            last_position = stalls[i]
    if cows >= k:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1
print("Maximum minimum distance:", answer)

# Rotate an array
def rotate_array(arr, k):
    n = len(arr)
    if n == 0 :
        return arr
    k = k % n
    if k != 0:
        return arr[-k:] + arr[:-k]
    else:
        arr
arr = [1,2,3,4,5,6,7]
k = 4
print(rotate_array(arr,k))        

# move all zeros at the end 
def move_zero(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
    while pos < len(arr):
        arr[pos] = 0
        pos += 1
    return arr 
print(move_zero([0, 1, 2, 0, 3, 12]))   

# remove even or odd 
arr = [1,2,3,4,5,6,7,8,9]
even = []
for i in arr:
    if i % 2 == 0:
    # for odd --> if i % 2 != 0 
        even.append(i)
print(even)    

# count the number of zeros
arr = [0,1,0,4,0,8,9]
count = 0
for i in arr:
    if i == 0:
        count += 1
print(count)        

# Two sum
def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
print(two_sum([2,7,11,15], 9))

# Find the element with maximum frequency
freq = [1,2,2,3,2,4,5]
ans = 0
for i in freq:
    count = 0
    for j in range(i, len(freq)):
        if freq[i] == freq[j]:
            count += 1
        if count > ans:
            ans = count    
print(ans)   

# Problem: Find the index of a target in a sorted array. Return -1 if it is absent.
def find_index(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return - 1
print("found target at index:", find_index([1,2,5,7,9], 7)) 

# Problem: Return the index where the target is found. If it is absent, return the index where 
# it should be inserted to keep the array sorted.
def insert_index(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low 
print(insert_index([0,1,3,4], 2))
print(insert_index([1,2,5,6], 7))
print(insert_index([1,2,3,4,5], 3))   

# Problem: A sorted array has been rotated. Find the target in (O(log n)) time.
def rotated_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1            
print(rotated_search([4,5,6,7,0,1,2], 1))  

# Problem: Koko has piles of bananas. She eats at speed k bananas per hour. 
# Each pile takes [pile / k] hours, and she can eat from only one pile per hour. 
# Find the minimum speed needed to finish within h hours.
