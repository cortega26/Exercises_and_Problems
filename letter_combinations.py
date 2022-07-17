# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

def letterCombinations(digits):
    """
    Given a string containing digits from 2-9 inclusive, return all 
    possible letter combinations that the number could represent. 
    Return the answer in any order.
    A mapping of digits to letters (just like on the telephone 
    buttons) is given below. Note that 1 does not map to any letters.
    """
        
    if digits == "":
        return []
        
    md = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
          '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
          '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
          '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    arr = [md[i] for i in digits] 
    n = len(arr)
    sol = []
    indices = [0 for i in range(n)]

    while True:
        sol.append(''.join(map(str, ([str(arr[i][indices[i]]) for i in range(n)]))))
        next = n - 1
        while next >= 0 and indices[next] + 1 >= len(arr[next]):
            next -= 1
        if next < 0:
            return sol
        indices[next] += 1
        for i in range(next + 1, n):
            indices[i] = 0
            

if __name__ == "__main__":
    letterCombinations('9876')
