menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
menuChk = ['1','2','3','9']

print('='*15, '메뉴선택', '='*15)
print('\t')
for i in range(len(menu)):
	print(menu[i], end = ' ')
print('\n')
print('='*40)

while True:
	n = input('{0:^20}'.format('메뉴의 번호를 선택해주세요.'))
	if n < 4:
		print('       %s Algorithm Chk' % (menu[n-1]))
	elif n ==" ":
		print('Chk')
	elif n == 9:
		print(menu[3])
		break
	else:
		print('메뉴 안의 번호를 선택해주세요')

	