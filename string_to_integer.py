# https://leetcode.com/problems/string-to-integer-atoi/

def myAtoi(s):
    """
    The algorithm for myAtoi(string s) is as follows:
    1. Read in and ignore any leading whitespace.
    2. Check if the next character (if not already at the end of the 
    string) is '-' or '+'. Read this character in if it is either. 
    This determines if the final result is negative or positive 
    respectively. Assume the result is positive if neither is present.
    3. Read in next the characters until the next non-digit character or
    the end of the input is reached. The rest of the string is ignored.
    4. Convert these digits into an integer (i.e. "123" -> 123, 
    "0032" -> 32). If no digits were read, then the integer is 0. Change 
    the sign as necessary (from step 2).
    5. If the integer is out of the 32-bit signed integer range [-231, 
    231 - 1], then clamp the integer so that it remains in the range. 
    Specifically, integers less than -231 should be clamped to -231, 
    and integers greater than 231 - 1 should be clamped to 231 - 1.
    6. Return the integer as the final result.
    """

    numbers = [str(i) for i in range(10)]
    signs = ['+', '-']
    sol = ''
    for i in s:
        if i == ' ' and sol == '': pass
        elif i in signs and sol == '': sol += i
        elif i in numbers: sol += i
        else: break       
    if sol == '' or sol in signs:
        return 0
    sol = int(sol)
    if sol < -1 * (2**31):
        return -1 * (2**31)
    elif sol >= (2**31):
        return (2**31) - 1
    else:
        return sol
        
if __name__ == "__main__":
    myAtoi('   -42car aoo')
