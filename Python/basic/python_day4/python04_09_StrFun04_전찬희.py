# python04_09_StrFun04_전찬희.py

#왼쪽/오른쪽/양쪽 공백 지우기(lstrip/rstrip/strip)

a=' hi '
print(a)
print(a.lstrip()+'Chk')
print(a.rstrip()+'Chk')
print(a.strip()+'Chk')
print('-'*15)

#문자열 바꾸기(replace)

a = 'Life is too short'
print(a)
cng=a.replace('Life','Your leg')
print(cng)
print("-"*15)