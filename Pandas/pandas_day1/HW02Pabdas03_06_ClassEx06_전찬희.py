'''
# override
   - 상속받은 곳에서 부모 메소드 재정의
   - 현재 메소드 우선
'''

class FourCal:
	def __init__(self):
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

class SafeFourCal(FourCal):    # 0일 때 0을 return 받아서 오류가 안뜸
	def div(self):         
		if self.second == 0:
			return 0
		'''
		else:
			return super().div()
			'''

a = SafeFourCal(4,2)        

four = ['+','-','×','÷']
callist = [a.sum(),a.sub(),a.mul(),a.div()]

for i in range(len(callist)):
	print(a.first,four[i],a.second,'=',callist[i])









	