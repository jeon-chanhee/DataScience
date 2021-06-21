

menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]



idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

'''
1문제] dic 에 idList를 key값으로 하고, scoreList를 value값으로 할당
'''

dic = {}
deleteIDList = []
idx = 0;

def InputData():                       # InputData() 에 함수 지정 그러면 그냥 InputData() 자체가 함수가 됨
	for i in range(len(idList)):        # dic에 idList와 scoreList 할당
		dic[idList[i]]=scoreList[i]    # dic['key값'] = value값

def PrintList():
	print('\n')
	print('    학생목록')
	print('\n')
	for i in range(len(MenuList)):
		print('{0:^7}'.format(MenuList[i]), end = '')
		print()
		print('-'*70)
		kList = list(dic.keys())   # dic의 list화
		vList = list(dic.values())
	for j in range(len(dic)):
		print('%6s %7s %7s %7s' % (kList[j],vList[j][0],vList[j][1],vList[j][2]))




print('-'*70)
print('학생관리시스템v01')
print('-'*70)
for i in range(len(menu)):
	print(menu[i], end = '')
print('\t')
print('-'*70)

while True:
	n = int(input('번호 입력 :'))
	if n <5:
		print('%s Algorithm Chk' % menu[n-1])
		if n ==3:
			print(PrintList())
			
	elif n == 9:
		print('종료합니다')
		break
	else:
		print('메뉴 번호를 확인해주세요')


'''
2문제] 3번을 선택한 경우, dic의 값을 출력 
for k in dic.keys():
	print(k,dic[k][0],dic[k][1],dic[k][2])


'''
