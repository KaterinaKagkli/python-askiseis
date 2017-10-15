sheep_list = []
nights = 0
while True:
	nights += 1
	temp_list = []
	while True :
		x = input("Enter number of sheep.\nIf you want to proceed to the next night, please input '0'\n: ")
		if x == 0:
			break
		else:
			temp_list.append(x)
	
	sheep_list.append(temp_list)
	
	x = raw_input("Do you want to enter the original number of sheep and end the program?\nEnter yes or no\n: ")
	if x == "yes":
		sheep = input("Enter original number of sheep: ")
		break

sheep_lost = sheep - sum(sheep_list[nights - 1])
print("Sheep lost : " + str(sheep_lost))
	
		
		
