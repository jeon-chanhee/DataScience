#Python03_20_autoMachine_Step05Finish_전찬희.py

menu = ['orange','strawberry','peach','mango','grape']
money = [1000, 2500, 1500, 2000, 2000]

print('****** 홍익 대학교 과일 판매머신 V03 *******')

for num in range(1,6):
    print('#%2d번 %s %d 원' % (num, menu[num-1], money[num-1]))

print('#%2d번 종료' % (num+1))

print('=========================================')




while True :
	no = int(input('구매번호를 입력하세요.'))
	if no in range(1,6):
		print( menu[no-1], '는', money[no-1], '원입니다')
	elif no == 6:
		print('종료')
		break
	else:
		print('번호 확인 바람.')
	coin = int(input('코인을 투입하세요.'))
	print('투입된 금액은 %d원입니다'%coin)
	print('='*15)
	print('선택한 과일 : %s' % menu[no-1])
	print('받은금액 : %d원' %coin)
	print('==거스름돈==')
	if coin >= money[no-1]:
		change = coin - money[no-1]
		print('거스름돈 : %d원' % change)
	else:
		print('돈을 넣어주시길 바랍니다')



	
	