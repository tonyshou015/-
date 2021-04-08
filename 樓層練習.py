f=eval(input("請輸入大樓的樓層數:"))
print("本大樓樓層列表:")
i=1
if f<4: 
    f=f+1
else:
    f=f+2



for i in range(1,f):
    if i==4:
        continue
    print("{}樓".format(i))
