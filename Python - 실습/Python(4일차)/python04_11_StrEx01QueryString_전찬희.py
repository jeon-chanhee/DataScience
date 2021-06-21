'''

https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=
utf8&query=python

URL
QueryString
    where=nexearch
	sm=top_hty
	fbm=1
	ie=utf8
	query=python
QueryString 개수 5개

'''

print('QueryString')
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=python'
str1 = (url.split('?'))
str2 = (str1[1].split('&'))
for i in range(len(str2)):
	print('\t',str2[i])
print('QueryString 개수 : %d개' % len(str2))


'''
print(b[0],'\n')
print(b[1],'\n')
print(b[2],'\n')
print(b[3],'\n')
print(b[4],'\n')

print('QueryString 개수 : %d개' % len(b))
'''