# 실습문제 4.3.1
# 사용자로부터 2개의 숫자를 입력 받고, 더한 결과를 출력하기

# - 표준 입력
# 첫번째 숫자를 입력하세요>>>20
# 두번째 숫자를 입력하세요>>>40
x = int(input("첫번째 숫자를 입력하세요>>>"))
y = int(input("두번째 숫자를 입력하세요>>>"))

# 자료형 확인하기 :tpye(x)
# str = string = 문자열

# 숫자형으로 변환
# int 함수를 사용 : int(데이터)

result = x + y
print(result)


## - 다른 풀이
# x = input("첫번째 숫자를 입력하세요>>>")
# y = input("두번째 숫자를 입력하세요>>>")

# result = int(x) + int(y)
# print(result) 