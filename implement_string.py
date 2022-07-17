# https://leetcode.com/problems/implement-strstr/

 def strStr(haystack, needle):
    """
    Given two strings needle and haystack, return the index of the first
    occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Clarification:
    What should we return when needle is an empty string? This is a great 
    question to ask during an interview.
    For the purpose of this problem, we will return 0 when needle is an 
    empty string. This is consistent to C's strstr() and Java's indexOf().
    """
    if needle == "":
        return 0
        
    if needle not in haystack:
        return -1
        
    needle_size = len(needle)    
    for i in range(len(haystack)):
        if haystack[i:i+needle_size] == needle:
            return i
        
if __name__ == "__main__":
    srtStr('thehorseisrunningintheshadow', 'run')
