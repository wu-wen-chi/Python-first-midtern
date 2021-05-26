T=int(input('輸入班級數(1≤T≤10):'))
a=[]
for i in range(1,T+1):
    t=int(input())
    a.append(t)
print("須購買的電腦數量:",max(a))