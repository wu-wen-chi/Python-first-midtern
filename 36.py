n=int(input('整數n:'))
cycl=1
print('數列:',end='')
while n != 1:
    if(n%2==1):
        n=n*3+1
        print(int(n),end=' ')
        cycl+=1
    else:
        n=n/2
        cycl+=1
        print(int(n),end=' ')
print("")
print('cycle length:%d' %(cycl))