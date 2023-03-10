# - 실습문제 5.3.4
# 성민은 대학교에 Lily 라는 이름의 교환학생과 친해지게 되었다. 
# 영어를 잘하지 못했던 성민은, Lily에게 한국어를 가르쳐 주기 위해 
# 한국어 연습 프로그램을 만들게 되었다. 

# - Learning Korean ver 2.0 - 
# 1. 연습할 한국어가 담긴  리스트를 만든다. 
# 2. 리스트에서 순서대로 단어를 가져와 화면에 출력한다.
# 3. 프로그램 사용자는 단어를 그대로 입력하고
# 4. 맞추면 다음 단어를 가져온다. 틀리면 프로그램 종료. 


word_list = ["사랑해", "귀엽다", "고마워", "행복해"]

# 점수
score = 0

print("Let's Learning Korean")
for word in word_list:
    print(word)
    data = input()
    if data == word: # 문제를 맞힌 경우
        score += 1 # 점수를 1 증가
        
print("전체 문제 개수 : ", len(word_list))
print("맞힌 개수 : ", score)
print("틀린 개수 : ", len(word_list) - score)

# 전체 문제 개수 : 4개
# 맞힌 문제 개수 : 2개
# 틀린 문제 개수 : 2개