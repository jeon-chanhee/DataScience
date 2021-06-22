'''
## 경로
- 절대 경로
    디스크... C:\ D:\폴더\파일명
- 상대 경로
   현재위치 : . 현재경로  .. 상위 경로

함수 < 모듈 < 팩키지 < 라이브러리

## 클래스
     틀 , 구조
	 함수 + 속성
     - 거푸집:
     -> 객체: 클래스로부터 생성
	 생성자: 함수, 클래스이름과 동일한 메서드, 주로 초기화에 사용
          ex) a = fourcal()   <---- 생성자

## 클래스 사용
 - 객체 생성후 사용
 - 사용하는 형식 : 객체.속성, 객체.함수 
'''

class Fourcal:
	def setdata(self,first,second):   # self는 현재 객체 Fourcal을 나타냄 
		self.first=first              # 현재 이 형태는 전체적인 틀을 나타냄
		self.second=second            # 객체를 만들어내는 틀. 즉 붕어빵 기계 같은 느낌

a = Fourcal()     # <------ 생성자 a는 객체 class가 붕어빵 기계라면 a는 붕어빵
a.setdata(4,2)    # fourcal에 대한 a를 생성해야 쓸 수 있음.

print(a.first)
print(a.second)
print(type(a))