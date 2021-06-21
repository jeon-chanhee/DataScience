#Python03_11_StarEx00_전찬희.py

'''
for 문 : 반복문
다중 for 문... 2중

for 문 안에 for문

outer for << 1ghl
     inner for

	 outer : 행
	 inner : 열

'''


for i in range(1,6):
	for j in range(0,i):
	    print('*', end = '')
	print ('\n')


'''
	      outer i        inner j
*            1                 1         range(0,1)      
**          2                 2        range(0,2)
***        3                 3        range(0,3)
****      4                  4        range(0,4)
*****    5                  5        range(0,5)      range(0,i)
'''