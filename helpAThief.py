# Level: Basic
# You have to help a thief to steal as many as GoldCoins as possible from a GoldMine.
# There he saw N Gold Boxes an each Gold Boxes consists of Ai Plates each plates
# consists of Bi Gold Coins. Your task is to print the maximum gold coins theif can
# steal if he can take a maximum of T plates.
#
# Input:
# T = 3, N = 3 
# A = [1, 2, 3]
# B = [3, 2, 1]
# Output:
# 7
# Explanation:
# The thief will take 1 plate of coins from the first box and 2 plate of coins
# from the second box. 3 + 2 * 2 = 7.


def maxCoins(A, B, T, N):
    if T == 0:
        return 0
    coins = 0
    while T > 0:
        max_value = max(B)
        max_index = B.index(max_value)
        if T < A[max_index]:
            coins += T * B[max_index]
            return coins
        coins += A[max_index] * B[max_index]
        T -= A[max_index]
        A.pop(max_index)
        B.pop(max_index)
        if len(A) == 0:
            break
    return coins
