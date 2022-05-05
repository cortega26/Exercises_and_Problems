
import time
import math
start_time = time.time()

def Palindrome(Strnum):
    for i in range(len(Strnum) // 2):
        if Strnum[i] != Strnum[-1 - i]:
            return False
    return True


def CutInHalf(Strnum):
    Half1b=0
    cont=0       
    for i in range(math.ceil(len(Strnum) / 2)):            
        cont+=1
        Half1b = (10 * Half1b) + int(Strnum[i])
    Half2b=Half1b
    test_num = test_numU = test_numL = 0
    if len(str(Strnum)) % 2 == 0:
        Upper=Half1b+1
        Lower=Half1b-1
        while Half2b > 0:
            remainder = Half2b % 10
            test_num = (test_num * 10) + remainder
            Half2b = Half2b//10
        while Upper > 0:
            remainder = Upper % 10
            test_numU = (test_numU * 10) + remainder
            Upper = Upper//10
        while Lower > 0:
            remainder = Lower % 10
            test_numL = (test_numL * 10) + remainder
            Lower = Lower//10
        A=(Half1b*(10**(cont)))+test_num
        B=((Half1b+1)*(10**(cont)))+test_numU
        C=((Half1b-1)*(10**(cont)))+test_numL
    else:        
        Upper=Half2b+1
        Lower=Half2b-1
        while Half2b > 0:
            remainder = Half2b % 10
            test_num = (test_num * 10) + remainder
            Half2b = Half2b//10
        while Upper > 0:
            remainder = Upper % 10
            test_numU = (test_numU * 10) + remainder
            Upper = Upper//10
        while Lower > 0:
            remainder = Lower % 10
            test_numL = (test_numL * 10) + remainder
            Lower = Lower//10
        test_numnew = test_numUnew = test_numLnew = 0
        if len(str(Half1b))==len(str(test_numU)):
            test_numU=str(test_numU)
            for i in range(len(test_numU)):
                test_numUnew=int(test_numU[1:i]+test_numU[i:])
        else:
            test_numUnew=test_numU
        if len(str(Half1b))==len(str(test_num)):
            test_num=str(test_num)
            for i in range(len(test_num)):
                test_numnew=int(test_num[1:i]+test_num[i:])
        else:
            test_numnew=test_num
        if len(str(Half1b))==len(str(test_numL)):
            test_numL=str(test_numL)
            for i in range(len(test_numL)):
                test_numLnew=int(test_numL[1:i]+test_numL[i:])
        else:
            test_numLnew=test_numL             
        B=(Half1b*(10**(cont-1)))+test_numnew
        C=((Half1b+1)*(10**(cont-1)))+test_numUnew
        A=((Half1b-1)*(10**(cont-1)))+test_numLnew        
    #print(A,B,C)
    #print(abs(A-N))
    #print(abs(B-N))
    #print(abs(C-N))
    if abs(A-N) <= abs(B-N) and (A-N) <= abs(C-N):
        return A
    elif abs(B-N) <= abs(A-N) and abs(B-N) <= abs(C-N):
        return B
    else:
        return C
    
                
def convertNumIntoString(N):
	Strnum = str(N)
	return Strnum        


def ClosestPalindrome(N):
    change=-1
    for i in range (N):    
        if Palindrome(convertNumIntoString(N)) == True:
            return N
            break
        else:
            N=N+change
            if change > 0:
                change+=1
                change=-change
            else:
                change-=1
                change=-change

#T=int(input())
T=1
for i in range(T):
    #N=int(input())
    N=941648184679874984126489754681841478988811111
    if N == 0:
        print("0")        
    elif N < 100:
        print(ClosestPalindrome(N))
        
    else:
        print((CutInHalf(convertNumIntoString(N))))
print("--- %s seconds ---" % (time.time() - start_time))        
