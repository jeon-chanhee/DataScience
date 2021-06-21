
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

# Q1
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#Q2 
no = 0
while True:
	no = no + 1
	if no > 1000:
		break