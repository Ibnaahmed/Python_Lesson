def fabonnacci(n):
    if(n>0):
        result=n+fabonnacci(n-1)
        print(result)
    else:
        result=0
    return result

print("Fabonnacci Sequence:")
n=int(input())
fabonnacci(n)