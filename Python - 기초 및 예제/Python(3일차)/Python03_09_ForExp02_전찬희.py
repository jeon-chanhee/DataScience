#Python03_09_ForExp02_전찬희.py
'''
print(10/3)  >>>>> 나누기 = 3.33333
print(10%3) >>>>> 나머지 연산자 = 1
print(10//3) >>>>>> // 정수로 보여줌 = 3

'''

a = [1,2,3,4]

result = [num * 3 for num in a if num % 2 == 0 ]

print(result)

'''
for num in a
        if num % 2 == 0     >>>> 2로 나누면 나머지 연산자 = 0 즉, 짝수
		    num * 3   
			의미 : 만약에 나눠서 나온 수가 짝수라면 * 3을 해주세요
'''

	