
import csv

marks = {}

#Read from csv file
with open('marksheet.csv', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		marks[ row[0] ] = row[1]

'''
Basic idea is to create 3 dictionary:
	- marks [ roll_no. ]
	- rank  [ marks ]
	- count [ marks ]
'''
count = {}
rank = {}

r = 1
l = 100000		# To avoid error for the first element in dict. marks
for m in sorted(marks.items(), key=lambda item:item[1] , reverse=True):
	rank[m[1]] = r

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
