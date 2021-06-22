'''
# 생성자(constructor)
# 상속 : 일반화된 재사용    일반화 = 부모 
** 클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스
이름을 넣어주면 된다.
형식] class 클래스 이름(상속할 클래스 이름)
'''

class FourCal:
	def __init__(self):    # 오버로드 같은 함수 2번쓰임
		pass
	def __init__(self,first,second):    
		self.first = first 
		self.second = second

	def sum(self):
		result = self.first+self.second
		return result
	
	def sub(self):
		result = self.first-self.second
		return result
	
	def mul(self):
		result = self.first*self.second
		return result
	
	def div(self):
		result = self.first/self.second
		return result

class MoreFourCal(FourCal):    # MoreFourCal을 추가로 상속받음. FourCal 에다가
	def pow(self,su01):        # 
		result = su01**2
		return result

a = MoreFourCal(4,2)          # 매겨변수 2개를 넣으면 생성되어서 바로 실행가능 setdata에 넣을 필요없이

four = ['+','-','×','÷']
callist = [a.sum(),a.sub(),a.mul(),a.div()]

for i in range(len(callist)):
	print(a.first,four[i],a.second,'=',callist[i])

print('제곱출력 : %d '% a.pow(5))







	