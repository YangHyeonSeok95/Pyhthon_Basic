# 1. 리스트 만들기
# - 데이터가 있는 리스트
animals = ["가물치", "벼메뚜기","비단뱀","도룡뇽"]

# - 데이터가 없는 리스트
empty = []

# 2. 리스트 조작하기

# - 데이터 접근하기
# 인텍스는 0부터 시작
print(animals[0]) # 가물치
print(animals[1]) # 벼메뚜기
print(animals[2]) # 비단뱀
print(animals[3]) # 도룡뇽

# - 데이터 추가하기
print("데이터 추가하기")
animals.append("고라니")
print(animals)

# - 데이터 할당하기
print("데이터 할당하기")
animals[1] = "청개구리"
print(animals) # 순서1번이 벼메뚜기에서 청개구리로 바뀜

# - 데이터 삭제하기
print("데이터 삭제하기")
del animals[0]
print(animals) # 인덱스0번인 가물치가 삭제됨 4개만 남음

# - 리스트 슬라이싱
print("데이터 슬라이싱")
print(animals[1:3])
print(animals[:]) # 전체
print(animals[:3]) # 처음부터 3까지
print(animals[1:]) # 1부터 마지막까지

# - 리스트 길이 
print("리스트 길이")
animals.sort()
print(animals)
animals.sort(reverse=True) #내림차순
print(animals)