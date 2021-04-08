f=eval(input("請輸入大樓的樓層數:"))

i=1
if f<4: 
    for i in range(1,f+1):
        print("{}樓".format(i))
else:
    for i in range(1,f+2):
        if i==4:
            continue
        print("{}樓".format(i))
    
