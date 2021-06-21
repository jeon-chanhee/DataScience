'''
4일차 실습 예제 02
조건] 
01. 10이상의 숫자를 입력 받는다.
02. 10이하의 숫자이면 '10이상의 숫자 확인 하세요'

03. 10이상이라면,
    -3 으로 나눠 떨어진 수 : Apple
	-4 으로 나눠 떨어진 수 : Melon
	-5 으로 나눠 떨어진 수 : Grape
	-8 으로 나눠 떨어진 수 : Strawberry 출력
'''

answer = []
fruitCnt = []


while True:
	n = int(input('10이상의 숫자를 입력하세요.[exit : 0]'))
	if n >= 10:
		print('FruitsList Algorithm Chk')
		print('==<<%s번 반복합니다>>==' % n)
		for i in range(1,n+1):
			if i%3==0:
				answer.append('Apple')
			if i%4==0:
				answer.append('Melon')
			if i%5==0:
				answer.append('Grape')
			if i%8==0:
				answer.append('StrawBerry')
			fruitCnt += answer
			if len(answer) == 0:
				print('%d.'% i)
			else:
				print('%d.' % i,str(answer))
			answer = []
		print('==<<Fruit Counter List>>==')
		print('Apple : %d회' % fruitCnt.count('Apple'))
		print('Melon : %d회' % fruitCnt.count('Melon'))
		print('Grape : %d회' % fruitCnt.count('Grape'))
		print('StrawBerry : %d회' % fruitCnt.count('StrawBerry'))
    
	elif n == 0:
		print('종료!')
		break
	else:
		print('10이상의 숫자 확인 하세요')
		continue





