#Python03_18_FormatEX02_전찬희.py

'''
%s 문자열
%c 문자 1개
%d 정수
%f 부동소수
%o 8진수
%x 16진수
%% 문자 % 자체

print'Error is %d%.' %98
     => Error is 98
'포맷코드형식'   % 값

'''


print('Error is %d' % 98)

print("%s" % "hi")
print("%10s" % "hi")         # 10은 처음부터 10자리 스페이스바 띄우기
print("%-10s" % "hi")


print("%f" % 3.42134234)
print("%0.4f" % 3.42134234)    # 0.4는 소수점 이하 4자리까지 나타냄.
print("%10.4f" % 3.42134234)   # 총 10자리를 잡고 소수점 이하 4자리 나타냄.