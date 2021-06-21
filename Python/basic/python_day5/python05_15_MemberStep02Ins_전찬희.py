menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
menuChk = ['1','2','3','9']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']



print('='*15, '메뉴선택', '='*15)
print('\t')
for i in range(len(menu)):
	print(menu[i], end = ' ')
print('\n')
print('='*40)


memberlist = []

while True:
	n = int(input('{0:^30}'.format('메뉴의 번호를 선택해주세요.')))
	if n<4:
		print('\t')
		print('       %s Algorithm Chk' % (menu[n-1]))
		print('\t')
		if n == 1:
			print('               SignUp')
			MID = input('ID :')
			Mpwd = input('PWD :')
			Mname = input('NAME :')
			Memail = input('EMAIL :')
			Mphone = input('PHONE :')
			Maddress = input('ADDRESS :')
			
			memberlist.append([MID,Mpwd,Mname,Memail,Mphone,Maddress])
			print('\t')
			print(memberlist, '\n','현재 회원수는 %d명입니다.' % len(memberlist))
			print('\t')
			
			
		
	elif n == 9:
		print(menu[3])
		break
	else:
		print('메뉴 안의 번호를 선택해주세요')

	