#Replace all 0's with 5 for a given integer
#Practice problem for geeksforgeeks.org

def ConvertFive(n):
    cont=0
    a=str(n)
    c=len(a)
    nf=0
    for i in a:
        cont+=1
        lugar=c-cont
        b=int(i)
        if b==0:
            b=5
        else:
            pass
        nf=nf+b*10**(lugar)
    print("initial number is: ",n)
    print("final number is: ",nf)
    
n=int(input("insert number: "))
ConvertFive(n)
