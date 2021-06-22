# lamda

'''
lamda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.
보통 함수를 한줄로 간결하게 만들 때 사용한다.
def를 사용해야할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.

사용형식]
    lamda 매개변수1, 매개변수2,...:매개변수를 이용한 표현식
'''

add= lambda a,b:a+b     # 식 = lambda 변수:결과값
add(3,4)
print(add)


def add(a,b):     # 이 함수와 같은 의미
	return a+b
result1= add(3,4)
print(result1)

# lamda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려준다.