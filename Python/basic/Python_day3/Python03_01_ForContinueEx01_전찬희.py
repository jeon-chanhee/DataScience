#Python03_01_ForContinueEx01_전찬희.py

marks = [90, 25, 67, 45, 80]

number = 0
 
for mark in marks:
	number = number + 1
	if mark < 60:
		continue

	print( number, ' 번 학생 축하합니다. 합격입니다.')


'''
mark = []
number = 0

for mark in marks:
	number = number + 1
	if mark < 60:
		continue
	
	print( number , '번 학생 축하합니다. 합격입니다.')


'''