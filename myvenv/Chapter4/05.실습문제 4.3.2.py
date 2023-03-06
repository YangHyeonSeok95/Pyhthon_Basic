# 실습문제 4.3.2
# 사용자로부터 태어난 연도를 입력 받으면, 현재 나이를 출력하기

# - 표준 입력 
# 태어난 연도를 입력하세요>>> 1994

# - 표준 출력
# 현재 나이는 28세입니다.

# 1. 연도 입력받기
# 2. 연도 int변환
# 3. 현재 연도 - 입력받은 연도
# 4. 결과 출력

from datetime import datetime
now = datetime.now()

birth = int(input("태어난 연도를 입력하세요>>>"))

year = now.year - birth + 1

print(f"현재나이는 {year}세 입니다.")

## - 다른 풀이
# year = int(input("태어난 연도를 입력하세요 >>>"))
# age = 2023 - year + 1
# print("현재나이는", age, "세 입니다.")