# RECURSION


# ARRAYS
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
s = 0
for i in range(len(x)):
    s += x[i]
print(s)           


# Q.4] find second max element in an array
arr = 2,7,8,14,13,9
max1 = arr[0]
max2 = arr[0]
for i in arr:
    if i > max1:
        max1 = i
    elif i > max2 and i != max1:
        max2 = i
print(max2)

# Q.5] two element sum 
ar = 2,7,4,9,1,6,5
target = 14
#  lets solve this using nested loops --- TC = O(n^2)
for i in range(len(ar)):
    for j in range(i+1,len(ar)):
        if ar[i] + ar[j] == target:
            print(ar[i], ar[j])  

# maximun subarray sum 



# count element with max frequency
k = [1,2,2,3,4,3,2]    # solved using loops T.C = o(N^2) and S.C o(1)
ans = 0
for i in k:
    count = 0
    for j in range(i,len(k)):
        if k[i] == k[j]:
            count += 1
        if count > ans:
            ans = count
print(ans)        

# now we will sort the array first
freq = [1,2,2,3,4,3,2]
freq.sort()
Count = 1
Ans = 1
for i in range(1, len(freq)):
    if freq[i] == freq[i-1]:
        Count += 1
    else:
        Count = 1     
    if Count > Ans:
        Ans = Count
print(Ans)  


# Rotate an Array
nums = [1,2,3,4,5,6,7,8]
# k = 3 means we have to shift last 3 digits in front


