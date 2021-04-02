import random
x=random.randint(1,10)

y=eval(input("請猜一個數字(1~10):"))
       


while y>x:
    print("太大了，小一點")
    y=eval(input("請猜一個數字(1~10):"))

else:
    print("太小了，大一點!")
    y=eval(input("請猜一個數字(1~10):"))
    
print("猜對了")
    
