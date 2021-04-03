x=eval(input("請輸入 n值，我幫您算n階乘:"))

if x!=0:
    e=x
    z=(x-1)
    while z>0:
        
        x=x*z
        z-=1
  
    else:
        print("{0}!={1}".format(e, x))
        
    if x<0:
        print("不符合輸入值，n應該大於等於0")
    
else:
    print("0!=1")
