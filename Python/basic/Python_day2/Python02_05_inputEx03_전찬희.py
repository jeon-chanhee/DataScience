# 1.실행시 2개의 값을 입력. 인풋함수 2번
# 2. vId, vPwd
# 3. id가 "Orange" 이고, pwd 가 "HappyDay" 이면
# "반갑습니다. 회원님" 아니면, "회원가입 확인 하세요"

vId = input('ID :')
vPwd = input('Pwd :')
if vId == "Orange" and vPwd == "HappyDay":
    print("반갑습니다. 회원님")
else :
	print("회원가입 확인 하세요")