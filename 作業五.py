year=eval(input("請輸入一個年份:"))

if (year%400 == 0) or ((year%4 == 0) and (year%100 != 0)):
    print("閨年")
    

else:
    print("平年")
    
