x=int(input("請輸入度數:"))
s=0
w=0
for i in range(1,x+1):
    if i<=120:
        s+=2.10
        w+=2.10
    elif i>120 and i<=330:
        s+=3.02
        w+=2.68
    elif i>330 and i<=500:
        s+=4.39
        w+=3.61
    elif i>500 and i<=700:
        s+=4.97
        w+=4.01
    elif i>700:
        s+=5.63
        w+=4.50
print("Summer months:%0.2f" %s)
print("Non-Summer months:%0.2f" %w)