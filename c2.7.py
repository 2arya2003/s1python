n=int(input("enter the number of terms:"))

a,b=0,1
if n<=0:
    print("plese enter a positive integer.")
elif n==1:
    print("fibonacci series up to 1 term:")
    print(a)
else:
    print("fibonacci series:")
    for i in range(n):
        print(a, end="")
        a, b=b, a+b