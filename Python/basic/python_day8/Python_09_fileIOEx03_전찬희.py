'''
# 프로그램의 외부에 저장된 파일을 읽는 여러가지 방법
1. readline() 함수 이용하기
   - 첫 번째 줄 읽어 출력
2. readlines() 함수 사용하기
   - 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
3. read 함수 사용하기
   - 파일의 내용 전체를 문자열로 돌려준다.
'''

# 2. readlines 함수 사용하기  # 텍스트 파일 리스트화!!

f = open('새파일.txt','r')
lines = f.readlines()
print(lines)

for line in lines:
	print(line)
f.close()