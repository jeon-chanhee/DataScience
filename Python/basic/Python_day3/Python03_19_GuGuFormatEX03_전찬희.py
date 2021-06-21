#Python03_19_GuGuFormatEX03_전찬희.py

for i in range(2,10):
	print('#%d단' % i, end = " ")
print('\n\n')
print('='*70)

for a in range(2,10):
	for b in range(2,10):
		print("%dx%d = %2d" %(b,a,b*a),end = ' ')
	print('\n\n')

print('-'*70)