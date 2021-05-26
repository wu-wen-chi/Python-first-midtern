n=int(input("輸入查詢組數n為:"))
for i in range(1,n+1):
    a,b=input("帳號 密碼:").split()
    if a=="123" and b=="456":
        print("9000")
    elif a=="456" and b=="789":
        print("5000")
    elif a=="789" and b=="888":
        print("6000")
    elif a=="336" and b=="558":
        print("10000")
    elif a=="775" and b=="666":
        print("12000")
    elif a=="556" and b=="221":
        print("7000")
    else:
        print("error")