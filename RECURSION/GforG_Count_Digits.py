# Given a non-negative integer s represented as a string, count the number of digits in 
# s that divide the number represented by s.
# A digit is considered valid only if it is non-zero and the number represented by s is 
# divisible by that digit.
# If a digit appears multiple times in s, each occurrence should be counted separately.

# Examples:
# Input: s = "35"
# Output: 1
# Explanation: The digit 5 divides 35, but the digit 3 does not. So the answer is 1.
# Input: s = "1122324"
# Output: 7
# Explanation: Every digit in "1122324" divides 1122324. So the answer is 7.

def divisibleByDigits(s):

    # Variable to count how many digits divide the number
    count = 0

    # Loop through every digit of the string
    # For "35", digit will be '3' and then '5'
    for digit in s:

        # Convert the current digit from string to integer
        # Example: '3' -> 3
        d = int(digit)

        # If digit is 0, skip it
        # We cannot divide by 0
        if d == 0:
            continue

        # Store the remainder while calculating the number
        remainder = 0

        # Loop through every digit of the number
        # For "35": i = '3', then i = '5'
        for i in s:

            # Build the number's remainder digit by digit
            #
            # For d = 3:
            # First:  (0 * 10 + 3) % 3 = 0
            # Second: (0 * 10 + 5) % 3 = 2
            #
            # Therefore 35 % 3 = 2
            remainder = (remainder * 10 + int(i)) % d

        # If remainder is 0, the number is completely
        # divisible by the current digit
        if remainder == 0:

            # Increase the count
            count += 1

    # Return the total number of digits that divide the number
    return count


# Call the function with "35"
# 35 is divisible by 5 but not by 3
print(divisibleByDigits("35"))

# Output:
# 1
