# m[roll] = marks
# m[marks] = count
# m[marks] = rank
import csv

marks = {}

with open('test.csv', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		marks[ row[0] ] = row[1]

count = {}
rank = {}

r = 1
l = 100000
for m in sorted(marks.items(), key=lambda item:item[1] , reverse=True):
	rank[m[1]] = r
	print (m)

	if(m[1] != l):
		count[m[1]] = 1
		if(l != 100000):
			r += count[l]
		else:
			r += 1		
	else:
		count[m[1]] += 1



	l = m[1]


while True:
	qr = input("Enter Roll Number: ")
	if(qr == "stop"):
		break;

	print("Marks:", marks[qr], ", Rank:", rank[ marks[qr] ], ", Tied Between:", count[ marks[qr] ])
