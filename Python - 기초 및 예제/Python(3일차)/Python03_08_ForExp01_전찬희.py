#Python03_08_ForExp01_전찬희.py


a = [1,2,3,4]
result = []
for num in a:
	result.append(num*3)

print(result)

print("=" * 30)

result = [num * 3 for num in a]
print(result)

	#[3,6,9,12]