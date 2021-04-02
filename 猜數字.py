import random
anser=random.randint(1,10)

guss=eval(input("請猜一個數字(1~10):"))
       


while guss!=anser:
    if guss<anser:
        print("太小了，大一點")

    else:
        print("太大了，小一點!")
    guss=eval(input("請猜一個數字(1~10):"))
    
else:
    print("猜對了")
    
