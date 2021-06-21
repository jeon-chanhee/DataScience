#Python03_06_GuGuDanEX03_전찬희.py

'''
for 문 : 반복문
다중 for 문... 2중

for 문 안에 for문

outer for << 1ghl
     inner for
'''


for i in range(2,4): # 2,              3
	print('outer :' , i)
	for j in range(1,4): # 1, 2, 3    1, 2 ,3
	    print('inner :', j, end = ' ')   
	print ('')