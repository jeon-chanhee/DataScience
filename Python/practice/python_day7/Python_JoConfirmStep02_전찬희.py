'''
# input() 함수 이용       
      결과 : 4인 이상의 이름을 입력하세요.( SB:spacebar로 구분한다) : 보라돌이,나나
	  - 4인이 아니면 ==> ^ 명수를 확인 하세요(4인 이상)
	  - 4인 이상이라면 ==> '보라돌이 나나 뚜비 뽀오' 입력되었습니다.

# 조건 1
   - 4인 이상 len() 인원수 반환
   - 5명 -> 1 ~ 5 
   - 중복 없이 반환.

Sample Run]
    보라돌이 뽀오 나나 뚜비
	  4     1   2  3     2중 for문 들어가야함

for idx in range(5):
	random 값 반환     ----->
	for idx in range(5): # 앞쪽과 비교하는 for문 찾기
           앞쪽비교 idx-1 -----> 똑같으면 앞으로 가야하니까
    list01[4,4]  -----> 앞 숫자와 비교해서 똑같으면 다시 되돌아가기
'''




NameList = []
import random


while True:
	NameList = input('4인 이상의 이름을 입력하세요. SB로 구분')
	NameList.split(' ')
	if len(NameList) >= 4:
		print('%s 입력되었습니다' % NameList)
		
		ranNum = random.randint(1,len(NameList))
		sumNum = []
		sumNum.append(ranNum)
		
		# namelist는 알아서 출력해 주세요
		# 입력받은 namelist의 크기를 len으로 반환해서 숫자를 중복 없이 출력
		# 새로운 숫자형 리스트를 만들어서 여기에 랜덤한 숫자를 계속 넣어줌
		# 단, 안에 중복된 값이 있으면 continue를 통해 뛰어 넘기
		# 리스트 안에 있는 값을 알아내는 예제 a in [list]
		
		for idx in range(len(sumNum)+1):
			for idx2 in range(idx,len(sumNum)+1):
				if idx2 in sumNum:
					continue
				else:
					for i in range(len(sumNum)):
						print(i)
						
	else:
		print('명수를 확인하세요 (4인 이상)')



