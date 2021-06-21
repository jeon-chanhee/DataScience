'''
Collection Data Type : 1개이상의 값 저장.

List                   Set

|-----------|           
| |         |
| |         |
| |         |
|_|_________|

unique : 값 중복가능     중복 안됨

'''

# 형식 : 리스트명 = [요소1, 요소2, 요소3,...]

a = []
b = [1,2,3]
c = ['Life','is','too','short']
d = [1,2,'Life','is']
e = [1,2,['Life','is']]
#비어있는 리스트는 a=list[]으로 생성가능

#리스트의 인덱싱과 슬라이싱
a = [1,2,3]
print(a[0])
print(a[0]+a[2])
print(a[-1])
print('-'*15)

print(b[0]) # =1
print(b[0]+b[2]) # 4
print(b[-1]) # 3
print('-'*15)