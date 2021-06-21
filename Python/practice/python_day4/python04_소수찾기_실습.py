'''
[4일차 실습 예제01]

#소수 판별 프로그램 작성#

- 소수란?
	1과 자기 자신만으로 나누어 떨어지는 1보다 큰 양의 정수.
	이를테면 2,3,5,7,11,13,17,19,23,29,31...등은 모두 소수.

- 조건
1. 사용자로부터 20이상의 수를 입력받는다.
2. n<=20이면 '숫자확인하세요'
3. n>=20이면 소수 판별 출력

'''
n = int(input('20이상의 수를 입력하세요:'))
b = 0

if n >= 20:
	print("1 소수 %s"%"X")
	for i in range(2,n+1): # 무슨 수인지 확인하는수
		b = 0
		for j in (2,i+1): # 소수인지 아닌지 나누는 조건
			if i % j == 0:
				b = 1
			if b == 0:
				chk = "O"
			else:
				#b==1
				chk = "X"
		print("%d 소수 %s"%(i,chk))
			
else:
	print('숫자 확인하세요.')

'''
n = int(input('20이상의 수를 입력하세요'))
if n >= 20:
	for i in range(2,n+1):
		if i %1==0 and %i==0:
		print('%d 소수 %s'%(i,chk))

else:
	print('숫자 확인하세요')


while True:
	
	num =int(input("숫자를 입력하세요 :  [Exit : 0]"))
	
	if num==0:
		break
	
	elif num<20:
		print("20 이상의 수를 입력하세요")
	
	else:
		print("1.소수X")
		for j in range(2,num+1):
			a=0
			for i in range(2,j):
				if j % i==0:
					a=1
			if a==0:
				print("%d.소수O"%j)
			else:
				print("%d.소수X"%j)

'''  