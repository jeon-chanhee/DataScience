#Python02_16_AutoMachine_step03_전찬희.py

menu = ['orange','strawberry','peach','mango','grape']
money = [1000, 2500, 1500, 2000, 2000]

print('****** 홍익 대학교 과일 판매머신 V03 *******')

for num in range(0,5):
    print(num+1,"번.", menu[num], ":", money[num],"원")
print('6 번. 종료')

print('=========================================')




while True :
	no = int(input('구매번호를 입력하세요.'))
	if no == 1:
		print(menu[no-1],"는", money[no-1],' 원입니다')
	elif no == 2:
		print(menu[no-1],"는", money[no-1],' 원입니다')
	elif no == 3:
		print(menu[no-1],"는", money[no-1],' 원입니다')
	elif no == 4:
		print(menu[no-1],"는", money[no-1],' 원입니다')
	elif no == 5:
		print(menu[no-1],"는", money[no-1],' 원입니다')
	elif no == 6:
		print('종료')
		break
