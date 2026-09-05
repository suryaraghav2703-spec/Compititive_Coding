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
for i in arr:
    if i < min_element:
        min_element = i
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


