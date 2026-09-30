# Different Ways to Add Parentheses :--
# Given a string expression of numbers and operators, return all possible results from computing 
# all the different possible ways to group numbers and operators. You may return the answer in any order.

# Example 1:

# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# Example 2:

# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10

def differentwaystocompute(expression):
    ans = []
    for i in range(len(expression)):
        if expression[i] in "+-*/":
            left = differentwaystocompute(expression[:i])
            right = differentwaystocompute(expression[i+1:])
            for l in left:
                for r in right:
                    if expression[i] == "+":
                        ans.append(l + r)
                    elif expression[i] == "-":
                        ans.append(l - r)
                    elif expression[i] == "*":
                        ans.append(l * r)
                    elif expression[i] == "/":  
                        ans.append(l / r)
    if not ans:
        ans.append(int(expression))
    return ans

expression = input("Enter an Expression: ")
result = differentwaystocompute(expression)
print("Different Possible result: ", result)                        


# ============================================================
# DRY RUN: expression = "2-1-1"
# ============================================================

# Function call:
# diffWaysToCompute("2-1-1")
#
# expression = "2-1-1"
# ans = []

# ------------------------------------------------------------
# First call: diffWaysToCompute("2-1-1")
# ------------------------------------------------------------

# Loop starts:
# i = 0 -> expression[0] = '2'
# '2' is not an operator -> continue

# i = 1 -> expression[1] = '-'
# '-' IS an operator

# Split expression at index 1:
#
# left  = "2"
# right = "1-1"
#
# Now recursively calculate both sides:
#
# left  = diffWaysToCompute("2")
# right = diffWaysToCompute("1-1")


# ============================================================
# LEFT SIDE: diffWaysToCompute("2")
# ============================================================

# expression = "2"
# ans = []

# i = 0 -> expression[0] = '2'
# '2' is not an operator

# No operator was found, so:
# ans = [int("2")]
# ans = [2]

# return [2]


# ============================================================
# RIGHT SIDE: diffWaysToCompute("1-1")
# ============================================================

# expression = "1-1"
# ans = []

# i = 0 -> expression[0] = '1'
# '1' is not an operator

# i = 1 -> expression[1] = '-'
# '-' IS an operator

# Split at index 1:
#
# left  = "1"
# right = "1"
#
# Recursively calculate:
#
# left  = diffWaysToCompute("1")
# right = diffWaysToCompute("1")


# ------------------------------------------------------------
# LEFT: diffWaysToCompute("1")
# ------------------------------------------------------------

# No operator found.
# ans = [1]
# return [1]


# ------------------------------------------------------------
# RIGHT: diffWaysToCompute("1")
# ------------------------------------------------------------

# No operator found.
# ans = [1]
# return [1]


# ------------------------------------------------------------
# Combine left and right:
#
# left  = [1]
# right = [1]
#
# l = 1
# r = 1
#
# Operator = '-'
#
# l - r
# 1 - 1 = 0
#
# ans = [0]
#
# return [0]


# ============================================================
# BACK TO FIRST CALL: diffWaysToCompute("2-1-1")
# ============================================================

# We now have:
#
# left  = [2]
# right = [0]
#
# for l in left:
#     l = 2
#
# for r in right:
#     r = 0
#
# Operator = '-'
#
# l - r
# 2 - 0 = 2
#
# ans = [2]


# ------------------------------------------------------------
# Continue first loop
# ------------------------------------------------------------

# i = 2 -> expression[2] = '1'
# '1' is not an operator -> continue

# i = 3 -> expression[3] = '-'
# '-' IS an operator
#
# This creates the SECOND possible parenthesization:
#
# expression = "2-1-1"
#
# left  = "2-1"
# right = "1"


# ============================================================
# LEFT SIDE: diffWaysToCompute("2-1")
# ============================================================

# expression = "2-1"
# ans = []

# i = 0 -> '2'
# Not an operator

# i = 1 -> '-'
# Operator found

# left  = "2"
# right = "1"

# diffWaysToCompute("2") -> [2]
# diffWaysToCompute("1") -> [1]

# l = 2
# r = 1

# Operator = '-'
#
# 2 - 1 = 1
#
# ans = [1]
#
# return [1]


# ============================================================
# RIGHT SIDE: diffWaysToCompute("1")
# ============================================================

# No operator found.
# return [1]


# ============================================================
# BACK TO "2-1-1"
# ============================================================

# left  = [1]
# right = [1]

# l = 1
# r = 1

# Operator = '-'
#
# 1 - 1 = 0
#
# ans = [2, 0]


# ============================================================
# FINAL RESULT
# ============================================================

# return [2, 0]

# Therefore:
#
# 2 - (1 - 1) = 2
#
# (2 - 1) - 1 = 0
#
# Final answer:
#
# [2, 0]