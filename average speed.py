a=int(input("enter a value:"))
b=int(input("enter a value 2:"))
c=int(input("enter a value 3:"))
avg=(a+b+c)/3
print("avg=",avg)
if avg>a and avg>b and avg>c:
    print("%d is higher than %d,%d"%(avg,a,b,c))
elif avg>a and avg>b:
    print("%d is higher than%d,%d"%(avg,a,b))  
elif avg>a and avg>c:
    print("%d is higher than %d,%d"%(avg,a,c)) 
else:
    print("invalid input")         