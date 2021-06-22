# lambda 활용법

x = lambda a:a+10
print(x(5))

x = lambda a,b:a*b
print(x(5,6))

def myfunc(n):
	return lambda a:a*n

mydoubler = myfunc(2)         # myfunc의 a값의 2배를 곱해준다는 함수설정
print(mydoubler(11))

mytripler = myfunc(3)
print(mytripler(11))