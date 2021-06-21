'''
list01 = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
print(len(list01))
sum = 0
for jumsu in list01:
	sum = sum + jumsu


## 소수점이하 2자리 확인
print('합계 :',sum)
print('평균 :', sum/len(list01))

average = sum/len(list01)
print('평균 : %0.2f' % average)
'''


#Q2 
no = 0
sum =0
while no <= 1000:
	no = no + 1
	if no % 3 == 0:
		sum += no
print(sum)