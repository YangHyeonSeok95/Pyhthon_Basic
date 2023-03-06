# - 실습문제 5.1.4
# 프로그램 사용자로부터 국어, 수학, 영어 성적이 입력된다. 
# 세 과목의 평균점수가 80점 이상이면 합격이다. 
# 그런데 점수에 따라 합격 또는 불합격이 정해지는 프로그램에 오류가 발생했다.
# 80점 이상일 경우 불합격이 표시되도록 프로그램을 작성해보자.  
# (단, 0점 에서 100점 사이의 숫자를 입력하지 않으면
#  "잘못 입력하였습니다."를 출력하자)

# 1-1 표준 입력
# 국어 >>>95 
# 수학 >>>75 
# 영어 >>>100
# 1-2 표준 출력
# 불합격

# 2-1 표준 입력
# 국어 >>>55 
# 수학 >>>40 
# 영어 >>>70
# 2-2 표준 출력
# 합격

# 3-1 표준 입력
# 국어 >>>-1 
# 수학 >>>120 
# 영어 >>>85
# 3-2 표준 출력
# 잘못 입력하였습니다.

Korean = int(input("국어 >>>"))
English = int(input("영어 >>>"))
Math = int(input("수학 >>>"))

Average = (Korean + English + Math) / 3


# if all(map(lambda v: 0<=v<=100, [Korean, English, Math])): 이렇게 도 가능
if 0 <= Korean <= 100 and 0 <= English <= 100 and 0 <= Math <= 100:
    
    if Average >= 80:
        print("불합격")
    else:
        print("합격")
else:
    print("잘못 입력하였습니다.")
   
    
# - 다른풀이
# korean = int(input("국어 >>>"))
# english = int(input("영어 >>>"))
# math = int(input("수학 >>>"))

# total = korean + english + math 
# avg = total / 3
# # 방법 1
# # - 조건이 만족할 경우 중첩 조건으로 합격 조건문 만들기
# if 0 <= korean <= 100 and 0 <= english <= 100 and 0 <= math <= 100:
#     if avg >= 80:
#         print("불합격")
#     else:
#         print("합격")
# else:
#     print("잘못 입력하였습니다.")

# 방법 2
# if korean < 0 or korean > 100 or math < 0 or math > 100 or english < 0 or english > 100:
#     print("잘못 입력하였습니다.")
# elif avg >= 80:
#     print("불합격")
# else:
#     print("합격")