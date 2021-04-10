print("DNA序列包含A,T,G,C")
x=input("請輸入第一條DNA序列:").upper()
similar= ""
y=input("請輸入第二條DNA序列:").upper()    


DNA_Length=min(len(x), len(y))

isAllDNAOK= True


for i in range(0, DNA_Length):
    if(x[i] in "ATGC") and (y[i] in "ATGC"):

        if x[i] == y[i]:
            similar += "|"
        else:
            similar += " "
    else:
        isAllDNAOK= False
        break

if isAllDNAOK:
    print(x)
    print(similar)
    print(y)
    similarity=similar.count("|")/len(similar)
    print("相似度:{:.2%}".format(similarity))
else:
    print("無效的DNA字母，你的字母必須是 A,T,C,G 這四個字母其中之一")
    
