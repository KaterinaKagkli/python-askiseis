import pandas
from random import *
number_of_mines = input("Number of mines(maximum 100): ")
table = []
x = []
y = []
for i in range(number_of_mines):#random mine position
	randx = randint(0,9)
	randy = randint(0,9)
	j = 0
	while j < len(x):
		if randx == x[j] and randy == y[j]:
			randx = randint(0,9)
			randy = randint(0,9)
			j = 0
		else:
			j += 1
	x.append(randx)
	y.append(randy)


for i in range(10): #making layout/board
	row = []
	for j in range (10):
		row.append(0)
	table.append(row)
for i in range(number_of_mines):#placing mines
		table[x[i]][y[i]] = "x"
for i in range(10):
	for j in range(10):
		if table[i][j] != "x":
			if i == 0:
				if j == 0:
					if table[i][j+1] == "x":
						table[i][j] += 1
					if table[i+1][j+1] == "x":
						table[i][j] += 1
					if table[i+1][j] == "x":
						table[i][j] += 1
				elif j == 9:
					if table[i][j-1] == "x":
						table[i][j] += 1
					if table[i+1][j-1] == "x":
						table[i][j] += 1
					if table[i+1][j] == "x":
						table[i][j] += 1
				if j != 0 and j != 9:
					if table[i][j-1] == "x":
						table[i][j] += 1
					if table[i][j+1] == "x":
						table[i][j] += 1
					if table[i+1][j-1] == "x":
						table[i][j] += 1
					if table[i+1][j] == "x":
						table[i][j] += 1
					if table[i+1][j+1] == "x":
						table[i][j] += 1
				
			elif i == 9:
				if j == 0:
					if table[i-1][j] == "x":
						table[i][j] += 1
					if table[i-1][j+1] == "x":
						table[i][j] += 1
					if table[i][j+1] == "x":
						table[i][j] += 1
				elif j == 9:
					if table[i][j-1] == "x":
						table[i][j] += 1
					if table[i-1][j-1] == "x":
						table[i][j] += 1
					if table[i-1][j] == "x":
						table[i][j] += 1
				if j != 0 and j != 9:
					if table[i][j-1] == "x":
						table[i][j] += 1
					if table[i][j+1] == "x":
						table[i][j] += 1
					if table[i-1][j-1] == "x":
						table[i][j] += 1
					if table[i-1][j] == "x":
						table[i][j] += 1
					if table[i-1][j+1] == "x":
						table[i][j] += 1
			if j == 0:
				if i != 0 and i != 9:
					if table[i-1][j] == "x":
						table[i][j] += 1
					if table[i-1][j+1] == "x":
						table[i][j] += 1
					if table[i][j+1] == "x":
						table[i][j] += 1
					if table[i+1][j+1] == "x":
						table[i][j] += 1
					if table[i+1][j] == "x":
						table[i][j] += 1
			elif j == 9:
				if i != 0 and i != 9:
					if table[i-1][j] == "x":
						table[i][j] += 1
					if table[i-1][j-1] == "x":
						table[i][j] += 1
					if table[i][j-1] == "x":
						table[i][j] += 1
					if table[i+1][j-1] == "x":
						table[i][j] += 1
					if table[i+1][j] == "x":
						table[i][j] += 1
			if i != 0 and i != 9 and j != 0 and j != 9:
				if table[i-1][j-1] == "x":
					table[i][j] += 1
				if table[i-1][j] == "x":
					table[i][j] += 1
				if table[i-1][j+1] == "x":
					table[i][j] += 1
				if table[i][j-1] == "x":
					table[i][j] += 1
				if table[i][j+1] == "x":
					table[i][j] += 1
				if table[i+1][j-1] == "x":
					table[i][j] += 1
				if table[i+1][j] == "x":
					table[i][j] += 1
				if table[i+1][j+1] == "x":
					table[i][j] += 1
				
				
			
print(pandas.DataFrame(table))
	

