
# 문제1]

grade = [90,75,55]

sum = 0
for jumsu in grade:
	sum += jumsu
	average = sum/len(grade)
print('합계 : %d' % sum)
print('평균 : %0.2f' % average)



# 문제2]

b = 'a:b:c:d'
r = b.replace(':','#')
print(r)



# 문제 3] 자연수 13이 홀수인지 짝수인지 판별!

n = int(input('숫자입력'))
if n % 2 == 1:
	print('홀수 입니다')
elif n % 2 == 0:
	print('짝수 입니다')



# 문제 4] 881120-1068234

ID = ('881120-1068234')
print(ID[0:6])
print(ID[7:14])

str1 = ID.split('-')
print(str1[0])
print(str1[1])



# 문제 5] 주민번호 앞자리가 1,3은 남자 2,4는 여자를 나타내라


pin = input('주민번호를 입력하세요')
pin1 = pin.split('-')
if pin1[1][0] == '1' or pin1[1][0]== '3':
	print('남자입니다')
if pin1[1][0] == '2' or pin1[1][0]== '4':
	print('여자입니다')




# 문제 6]

c = [1,3,5,4,2]
c.sort()
c.reverse()
print(c)



# 문제 7]

d= ['Life','is','too','short']
print(' '.join(d))




# 문제8]

e = (1,2,3)
e = e + (4,)
print(e)





'''
문제 9]
a = dict()

a['name'] = 'python'
a[[1]] = 'python'     # 튜플은 수정이 불가능, 리스트는 수정가능 근데 
                      # 리스트형태가 들어갔기 때문에 오류가 뜸.
'''






