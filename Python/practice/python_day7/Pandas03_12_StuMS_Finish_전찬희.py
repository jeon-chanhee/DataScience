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
	
	for k in dic.keys():
		scoresum = (dic[k][0]+dic[k][1]+dic[k][2])
		scorediv = (scoresum/len(dic[k]))
		if scorediv >= 70:
			passchk = '합격'
		else:
			passchk = '불합격'
		print('%6s %6s %7s %8s %8s %8d %8s' % (k, dic[k][0],dic[k][1],dic[k][2],scoresum,scorediv,passchk))




def Mainpg():
	inputnum = int(input('번호를 입력해주세요'))
	if inputnum == 1:
		DelID()
	elif inputnum == 2:
		SignIn()
	elif inputnum == 3:
		PrintList()
	elif inputnum == 4:
		PassList()
	elif inputnum == 9:
		exit('메뉴를 종료합니다')
	else:
		print('없는 번호입니다. 다시 입력해주세요')

def DelID():
	deleID = input('ID를 입력해주세요 :  ')
	if deleID not in idList:
		print('해당 ID 없음')
	else:
		del dic[deleID]
		deleteIDList.append(deleID)
	

def SignIn():
	addID = input('ID 추가등록 :  ')
	
	if addID in deleteIDList:
		print('탈퇴회원 가입불가')
	else:
		addpilgi = int(input('필기점수 :  '))
		addsilgi = int(input('실기점수 :  '))
		addinsung = int(input('인성점수:  '))
		dic[addID]=[addpilgi,addsilgi,addinsung]


def PassList():
	print('%12s Algorithm Chk' % menu[3])
    
print('-'*70)
print('학생관리시스템v01')
print('-'*70)
for i in range(len(menu)):
	print(menu[i], end = '')
print('\t')
print('-'*70)

InputData()
while True:
    Mainpg()