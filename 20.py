a=[['123','Tom','DTGD'],['456','Cat','CSIE'],['789','Nana','ASIE'],['321','Lim','DBA'],['654','Won','FDD']]
b=int(input('輸入查詢學號為:'))
if b==123:
    c=a[0][0:3]
    cc=' '.join(c)
    print("學生資料為:",str(cc))
if b==456:
    d=a[1][0:3]
    dd=' '.join(d)
    print("學生資料為:",str(dd))
if b==789:
    e=a[2][0:3]
    ee=' '.join(e)
    print("學生資料為:",str(ee))
if b==321:
    f=a[3][0:3]
    ff=' '.join(f)
    print("學生資料為:",str(ff))
if b==654:
    g=a[4][0:3]
    gg=' '.join(g)
    print("學生資料為:",str(gg))