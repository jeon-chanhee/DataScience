'''
# input() 함수 이용       
      결과 : 4인 이상의 이름을 입력하세요.( SB:spacebar로 구분한다) : 보라돌이,나나
	  - 4인이 아니면 ==> ^ 명수를 확인 하세요(4인 이상)
	  - 4인 이상이라면 ==> '보라돌이 나나 뚜비 뽀오' 입력되었습니다.
'''




NameList = []


while True:
	NameList = input('4인 이상의 이름을 입력하세요. SB로 구분').split(' ')
	if len(NameList) >= 4:
		for i in range(len(NameList)):
			print('%s' % NameList[i],end = ' ')
		print('입력되었습니다')
	else:
		print('명수를 확인하세요 (4인 이상)')



