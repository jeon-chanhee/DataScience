'''
** Selection Sort
   1. 오름차순
      숫자: 작은 수 ---> 큰 수로 배열
	  영문: A ---> Z
	  한글: ㄱ ---> ㅎ

   2. 내림차순
      숫자: 큰 수 ----> 작은 수
	  영문: Z ----> A
	  한글: ㅎ ----> ㄱ
'''

sortNum = [2,5,6,1,2,8,33,77,12]

for idx in range(len(sortNum)-1):
	for idx2 in range(idx+1,len(sortNum)):
		if (sortNum[idx]>sortNum[idx2]):
			Tem=sortNum[idx]
			sortNum[idx]=sortNum[idx2]
			sortNum[idx2]=Tem
print(sortNum)	
	
'''	
	print("%d회차 :"%(idx+1),end =' ')
	for k in sortNum:
		print(k, end=' ')
	print()
'''			
#print(sortNum)
		
