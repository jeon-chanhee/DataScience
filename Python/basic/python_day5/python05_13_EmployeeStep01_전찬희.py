# 사번, 이름, 입사일, 급여
# 계약직, 정규직
# 사번 1번째
# T,t << 계약직
# R   << 정규직



TName = ["구분","사원명","입사일","급여"]

empInfo = [
      ['T160821',"캔디","2016-05-10"],
	  ['R160510',"장미","2016-05-10"],
	  ['t160811',"튤립","2016-08-15"],
	  ['T160821',"포도","2016-08-22"],
	  ['r160850',"사과","2016-08-30"] ]
'''
	 if empInfo[0][0][0] == 't' or empInfo[0][0][0] == 'T':
		 del empInfo[0][0]
		 empInfo[0].insert(0,"계약직")
	 elif empInfo[0][0][0] == 'r' or empInfo[0][0][0] == 'R':
		 del empInfo[0][0]
		 empInfo[0].insert(0,"정규직")
'''

empPayTable = [[250,10],[200,12],[300,9],[230,11],[150,12]]

# 인사 관리 시스템
'''
empInfo.upper(range(0,5))
Temployee = empInfo.find('T')
Remployee = empInfo.find('r')
'''

for i in range(len(TName)):
	print('%s     ' % TName[i],end='')
print('\n')
print('-'*50)

money = [0,0,0,0,0]

for i in range(len(empInfo)):
	A = empInfo[i][0].count('T')
	a = empInfo[i][0].count('t')
	B = empInfo[i][0].count('R')
	b = empInfo[i][0].count('r')
	money[i] = empPayTable[i][0]*empPayTable[i][1]

	if A == 1 or a == 1:
		empInfo[i][0]='계약직'
	if B == 1 or b == 1:
		empInfo[i][0]='정규직'
	print(empInfo[i][0], '\t',empInfo[i][1],'\t', empInfo[i][2], '\t', money[i])



'''
for i in range(0,len(empInfo)):
	if empInfo[i][0][0] == 'T' or empInfo[i][0][0] == 't':
		print('계약직 %10s %20s %10d' % (empInfo[i][1], empInfo[i][2],(empPayTable[i][0]*empPayTable[i][1])))
		print('\n')
	elif empInfo[i][0][0] == 'R' or empInfo[i][0][0] == 'r':
		print('정규직 %10s %20s %10d' % (empInfo[i][1], empInfo[i][2],(empPayTable[i][0]*empPayTable[i][1])))
		print('\n')
	else:
		pass

'''