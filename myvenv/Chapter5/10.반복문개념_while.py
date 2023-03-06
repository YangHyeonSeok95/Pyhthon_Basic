# -초기식
# while 조건식:
#     반복할 명령
#     증감식

# for = 반복할 횟수가 정해졌을 때 사용
# while = 반복할 횟수가 정해지지 않았을 때 사용한다.

i = 0
while i < 10: # 조건식
    print(i, "번째 다짐, 나는 할 수 있다!")
    i += 1 # 증감식
    
i = 5
while i < 9: # 조건식
    print(i, "번째 다짐, 나는 할 수 있다!")
    i += 1 # 증감식
    
i = 0
while i < 10: # 조건식
    print(i, "번째 다짐, 나는 할 수 있다!")
    i += 2 # 증감식
    
# 무한루프
# : 조건식에 Treu를 넣어서 항상 반복되게 만든 것.

while True:
    x= input("종료하려면 exit를 입력하세요 >>>")
    if x == "exit":
        break