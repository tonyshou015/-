#x=本金
#y=年利率
#z=期數
#e=本利和
x=eval(input("請輸入您的本金:"))
y=eval(input("請輸入您的年利率(如1.23=1.23%):"))
z=eval(input("請輸入您的期數(年)"))


d=y/100

t=1
for t in range(1,11):
    e=x*(1+d)**t
    print("您第{0}年的本利合為:{1:.2f}".format(t,e))
