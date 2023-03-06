# - 실습문제 5.2.2
# 턱걸이 평균 측정 프로그램을 만들어보자. 
# 먼저, 턱걸이 횟수를 저장할 빈 리스트를 만든다. 
# 그리고 일주일간의 턱걸이 횟수를 입력 받아 리스트에 저장한다. 
# 리스트에 저장된 데이터의 평균을 구해 출력한다.

# 표준 입력
# 1일차 턱걸이 횟수 >>>20
# 2일차 턱걸이 횟수 >>>23
# 3일차 턱걸이 횟수 >>>16
# 4일차 턱걸이 횟수 >>>14
# 5일차 턱걸이 횟수 >>>24
# 6일차 턱걸이 횟수 >>>27
# 7일차 턱걸이 횟수 >>>30

# 표준 출력
# 22

# chin_blow = [] # 빈 리스트 생성
# day = int(input()) # 날짜 입력
   
# for i in range(0, 7):
#     while day < 8:
#         x = int(input(f"{day}일차 턱걸이 횟수>>>"))
#         chin_blow.append(x)
# total = chin_blow[0] + chin_blow[1] + chin_blow[2] + chin_blow[3] + chin_blow[4] + chin_blow[5] + chin_blow[6]
# avg = total / 7

# print(int(avg))  

# - 다른풀이
chin_blow = [] # 빈 리스트 생성

x = int(input("1일차 턱걸이 횟수 >>>"))
chin_blow.append(x)
x = int(input("2일차 턱걸이 횟수 >>>"))
chin_blow.append(x)
x = int(input("3일차 턱걸이 횟수 >>>"))
chin_blow.append(x)
x = int(input("4일차 턱걸이 횟수 >>>"))
chin_blow.append(x)
x = int(input("5일차 턱걸이 횟수 >>>"))
chin_blow.append(x)
x = int(input("6일차 턱걸이 횟수 >>>"))
chin_blow.append(x)
x = int(input("7일차 턱걸이 횟수 >>>"))
chin_blow.append(x)

total = chin_blow[0] + chin_blow[1] + chin_blow[2] + chin_blow[3] + chin_blow[4] + chin_blow[5] + chin_blow[6]
avg = total / 7

print(int(avg))  

# - 다른풀이
# 반복문을 나타내 볼게요
# range(10) 은 0~9 까지 숫자를 포함하는 range 객체를 만들어준다.

chin_blow = [] # 빈 리스트 생성
for i in range(0, 7): 
    day = int(input())
    x = int(input(f"{day}일차 턱걸이 횟수 >>>"))
    chin_blow.append(x)
    
total = chin_blow[0] + chin_blow[1] + chin_blow[2] + chin_blow[3] + chin_blow[4] + chin_blow[5] + chin_blow[6]
avg = total / 7

print(int(avg))  

