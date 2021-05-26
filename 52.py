n=int(input('輸入n值:'))
a={}
for i in range(1,n+1):
    name=input('請輸入姓名:')
    mail=input('請輸入電子郵件:')
    a[name]=mail
s=input('請輸入要查詢電子郵件的姓名:')
if s in a:
    print('電子郵件帳號為:',a[name])