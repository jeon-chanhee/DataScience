#Python02_15_AutoMachine_step02_전찬희.py

menu = ['orange','strawberry','peach','mango','grape','종료']

print('****** 홍익 대학교 과일 판매머신 V02 *******')
print(num+1, menu[num])
print('=========================================')
while True :
    no = int(input('구매번호를 입력하세요.'))
    if no == 1:
        print('orange 1000원입니다')
    elif no == 2:
        print('strawberry 2500원입니다')
    elif no == 3:
        print('peach 1500원입니다')
    elif no == 4:
        print('mango 2000원입니다')
	elif no == 5:
		print('grape 2000원입니다')
	elif no == 6:
		print('종료')
		break