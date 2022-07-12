# Source: https://leetcode.com/problems/find-the-closest-palindrome/

def nearest_palindromic(n: str):
    """
    Given a string n representing an integer, return the closest integer 
    (not including itself), which is a palindrome. If there is a tie, 
    return the smaller one.
    """

    size = len(n)
    n = int(n)
    if size == 1:
        return str(n - 1)
    if size == 2 and str(n) == str(n)[::-1]:
        for i in range(1,6):
            if str(n - i) == str(n - i)[::-1]:
                return str(n - i)
            elif str(n + i) == str(n + i)[::-1]:
                return str(n + i)
        
    half = (size // 2) + size % 2 
    half_up = int(str(n)[:half]) + 1
    half_mid = int(str(n)[:half])
    half_down = int(str(n)[:half]) - 1
    if size % 2 == 0:
        up = int(str(half_up) + str(half_up)[::-1])
        mid = int(str(half_mid) + str(half_mid)[::-1])
        down = int(str(half_down) + str(half_down)[::-1])
    else:
        if len(str(half_up)) != half:
            up = int(str(half_up)[:-2] + str(half_up)[::-1])
        else:
            up = int(str(half_up)[:-1] + str(half_up)[::-1])
        mid = int(str(half_mid)[:-1] + str(half_mid)[::-1])
        if len(str(half_down)) != half:
            down = int(str(half_down) + str(half_down)[::-1])
        else:
            down = int(str(half_down)[:-1] + str(half_down)[::-1])

    min_diff = min(abs(n - up), abs(n - mid), abs(n - down))
    if min_diff == 0:
        min_diff = min(abs(n - up), abs(n - down))     
        
    if str(n - min_diff) == str(n - min_diff)[::-1]:
        return str(n - min_diff)
    else:
        return str(n + min_diff)

if __name__ == "__main__":
    nearest_palindromic('1234567890')
