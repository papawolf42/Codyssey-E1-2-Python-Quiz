"""
[실습 03] self에 속성 저장하기 (store attributes)

목표:
- 생성자 `__init__`와 `self`의 역할을 확인한다.

직접 작성:
1. `Quiz.__init__(self, question)`을 정의한다.
2. 전달받은 값을 `self.question`에 저장한다.
3. 서로 다른 문제를 가진 객체 두 개를 만든다.

통과 조건:
- 각 객체의 `question`이 전달한 문자열과 같다.
- 한 객체의 값을 바꿔도 다른 객체의 값은 바뀌지 않는다.

커밋 예: Study: self 속성 저장 연습
"""

# 이 아래에 직접 작성하세요.
class Quiz:
    def __init__(self, question):
        self.question = question

quiz1 = Quiz("질문 1")
quiz2 = Quiz("질문 2")

print(quiz1.question)
print(quiz2.question)
quiz1.question = "질문 1 수정"
print(quiz1.question)
print(quiz2.question)
