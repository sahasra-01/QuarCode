a = [[0]*5]*5

for i in range(5):
	for j in range(5):
		print(i, j)
		a[i][0] = i+j

print(a)