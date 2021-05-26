a=int(input("組數為:"))
pay=[]
for i in range(a):
    n=input("第"+str(i+1)+"組:").split()
    pay.append(int(n[0])*250+int(n[1])*175)
for i in range(a):
    print("第"+str(i+1)+"組應收費用為:"+str(pay[i]))