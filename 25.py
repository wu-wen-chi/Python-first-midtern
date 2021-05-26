s=""
while(s!="end"):
    s=input("檢測的字串(end 結束)")
    if(s=="end"):
        print("檢測結束")
    else:
        n=input("檢測的單一字元:")
        a=s.count(n)
    print("字元"+str(n)+"的出現次數為"+str(a))