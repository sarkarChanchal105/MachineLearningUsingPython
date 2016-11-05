

def fibo(a,b,i,n):
    if i<n:
        return fibo(b,a+b,i+1,n)
    else:
        return a,b


print(fibo(1,1,1,100))

print(fibo(354224848179261915075,573147844013817084101,1,100))