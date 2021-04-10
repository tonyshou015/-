import random

count=0
while True:
    x=random.randint(1,2)
    y=random.randint(1,2)
    count+=1
    if x==y:
        print("笑筊({0},{1})".format(x,y))
    else:
        print("聖筊({0},{1})".format(x,y))
        print("您擲了{}次才擲到聖筊".format(count))
        break
    
