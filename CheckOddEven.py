a = input("Enter the number")
while(a != 'q'):
	a = int(a)
	if a%2 == 0:
		print("a is even number")
	else:
		print("a is odd number")
	a = input("Enter the number")