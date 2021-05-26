n=input("輸入月租費形式及通話時間為:").split(",")
a1=int(n[1])*0.09
if int(n[0])==186 and a1<=186:
    print("通話費為:186")
a2=int(n[1])*0.09*0.9
if int(n[0])==186 and a2<=186*2:
    print("通話費為:",int(round(a2,1)))
a3=int(n[1])*0.09*0.8
if int(n[0])==186 and a3>=186*2:
    print("通話費為:",int(round(a3,1)))
    
b1=int(n[1])*0.08
if int(n[0])==386 and b1<=386:
    print("通話費為:386")
b2=int(n[1])*0.08*0.8
if int(n[0])==386 and b2<=386*2:
    print("通話費為:",int(round(b2,1)))
b3=int(n[1])*0.08*0.7
if int(n[0])==386 and b3>=386*2:
    print("通話費為:",int(round(b3,1)))
    
c1=int(n[1])*0.07
if int(n[0])==586 and c1<=586:
    print("通話費為:586")
c2=int(n[1])*0.07*0.7
if int(n[0])==586 and c2<=586*2:
    print("通話費為:",int(round(c2,1)))
c3=int(n[1])*0.07*0.6
if int(n[0])==586 and c3>=586*2:
    print("通話費為:",int(round(c3,1)))
    
d1=int(n[1])*0.06
if int(n[0])==986 and d1<=986:
    print("通話費為:986")
d2=int(n[1])*0.06*0.6
if int(n[0])==986 and d2<=986*2:
    print("通話費為:",int(round(d2,1)))
d3=int(n[1])*0.06*0.5
if int(n[0])==986 and d3>=986*2:
    print("通話費為:",int(round(d3,1)))