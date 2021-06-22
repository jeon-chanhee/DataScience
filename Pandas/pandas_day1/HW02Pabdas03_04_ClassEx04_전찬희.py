'''

하나의 클래스에 같은 이름의 메서드가 두개 이상: 오버로드
이름이 같다면 매개변수의 개수에 따라 구분함.

'__init__' 생성자

'''

class FourCal:
	def __init__(self):
		pass
	def __init__(self,first,second):    # self는 객체 first,second는 매개변수
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


# a =FourCal
# a.setdata(4,2)   
a = FourCal(4,2)    # 매겨변수 2개를 넣으면 생성되어서 바로 실행가능 setdata에 넣을 필요없이

four = ['+','-','×','÷']
callist = [a.sum(),a.sub(),a.mul(),a.div()]

for i in range(len(callist)):
	print(a.first,four[i],a.second,'=',callist[i])

	
