x=int(input("X軸座標:"))
y=int(input("Y軸座標:"))
a=(x**2+y**2)
if x>0 and y>0:
    print("該點位於第一象限,離原點距離根號"+str(a))
elif x>0 and y<0:
    print("該點位於第四象限,離原點距離根號"+str(a))
elif x<0 and y>0:
    print("該點位於第二象限,離原點距離根號"+str(a))
elif x==0 and y==0:
    print("該點位於原點")
else:
    print("該點位於第三象限,離原點距離根號"+str(a))