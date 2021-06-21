
# Key로 Value 얻기(get)

a = {'name':'pey', 'phone':'0119993323','birth':'1118'}
print(a.get('name'))
print('-'*15)

'''
get(x) 함수는 x라는 Key에 대응되는 Value를 돌려준다.
a['nokey']는 Key 오류를 발생시키고 a.get('nokey')는 None을
돌려준다는 차이가 있다.
'''
print(a.get('nokey'))
#print(a['nokey'])

print('-'*15)

