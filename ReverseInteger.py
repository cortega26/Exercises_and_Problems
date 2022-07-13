# https://leetcode.com/problems/reverse-integer/

def reverse(x):
    """
    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit 
    integer range [-2E31, 2E31 - 1], then return 0.
    """
    
    if x >= 0:
        x = int(str(x)[::-1])
    else:
        x = -1 * int(str(x)[1:][::-1])        
    if -1 * (2**31) <= x <= (2**31) - 1:
        return x
    else:
        return 0


if __name__ == "__main__":
    reverse(29328987689)                                                                                                                                                                                                                                                                      
