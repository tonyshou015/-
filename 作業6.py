h=eval(input("請輸入身高(cm):"))
w=eval(input("請輸入體重(kg):"))

BMI=w/((h/100)**2)

if BMI>=25:
    print("過重")

elif BMI>=18.5:
    print("正常")
    
else:
    print("過輕")
    
