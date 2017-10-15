x = input("Input number: ")
flag = False
for a in range(1, x):
	for b in range(a + 1, x):
		for c in range(b + 1, x):
			if (a**2 + b**2 == c**2) and (x == a + b + c):
				flag = True
				print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(c))
				
if flag == False:
	print("Cannot find pythagorean triple")