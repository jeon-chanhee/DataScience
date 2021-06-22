
class Fourcal:
	def setdata(self,first,second):   
		self.first=first              
		self.second=second
	
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
		
a = Fourcal()
	
a.setdata(4,2)

four = ['+','-','×','÷']
callist = [a.sum(),a.sub(),a.mul(),a.div()]

for i in range(len(callist)):
	print(a.first,four[i],a.second,'=',callist[i])
