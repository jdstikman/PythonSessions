print("The following program will print the table of the given input number")
x = input("Enter no: ")
x = int(x)
l = 1
while(l <= 10):
    v = (x * l)
    print("{} x {} = {}".format(x, l, v))
    l = (l + 1)
