#Python03_13_StarEx00_전찬희

for i in range(1,6):
	for j in range(i,6):
	    print('*', end = '')
	print ('\n')

'''
	       outer i        inner j
*****      1                 5         range(1,6)      1부터 5까지 5개 1층에 5개
****       2                 4         range(2,6)       2부터 5까지 4개 2층에 4개
***        3                 3        range(3,6)       3부터 5까지 3개 3층에 3개
**         4                 2        range(4,6)        4부터 5까지 2개 4층에 2개
*          5                 1        range(5,6)        5부터 5까지 1개 5층에 1개
                                                                 range(i,6)
'''

'''
다른 방식
count = int(input('열 갯수를 입력해 주세요:'))

for i in range(count, 0, -1):
	for j in range(i):
		print('*', end=' ')
	print()

print()
print()

오버로드(OverLoad) : 같은 이름의 함수가 여러개.
range(stop)   매개변수
range(start, stop)
range(start, stop, step)   << step : 단계 +이거나 -가 가능

'''