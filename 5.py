m=int(input("請輸入階層值Ｍ:"))
n=1
x=1
while x<m:
    x=(n+1)*x
    n=n+1
print("超過Ｍ為%d的最小階層Ｎ值為:" %m +str(n))