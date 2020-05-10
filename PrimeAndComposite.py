a = input("Enter the number")
a = int(a)
x = 2
IsPrime = True
while(x < a):
    if(a%x == 0):
        IsPrime = False
        break
    x = x+1
if(IsPrime):
    print("{} is a prime number".format(a))
else:
    print("{} is a composite number".format(a))