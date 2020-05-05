a = input("Enter number here")
a = int(a)
if a < 90:
    print("number is acute")
elif a == 90:
    print("right angle")
elif a > 90 and a < 180:
    print("obtuce")
else:
    print("i have no idea what you are talking about")