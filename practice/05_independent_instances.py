"""
[실습 05] 인스턴스별 상태 확인하기 (independent instances)

목표:
- 같은 클래스로 만든 객체가 각자 상태를 가진다는 점을 확인한다.
- 클래스 속성과 인스턴스 속성의 차이를 작은 실험으로 확인한다.

직접 작성:
1. 문제와 정답을 저장하는 `Quiz`를 만든다.
2. 정답이 서로 다른 객체 두 개를 만든다.
3. 같은 선택 번호를 두 객체의 `is_correct()`에 전달한다.
4. 심화: 클래스에 빈 리스트를 두었을 때 두 객체가 그 리스트를 공유하는지 확인한다.
5. 같은 리스트를 `self`에 만들었을 때 결과가 어떻게 달라지는지 확인한다.

통과 조건:
- 같은 입력에 한 객체는 `True`, 다른 객체는 `False`를 반환한다.
- 그 이유를 `self`를 사용해 설명할 수 있다.
- 심화: 가변 클래스 속성을 공유할 때 생기는 문제를 설명할 수 있다.

커밋 예: Study: 인스턴스별 독립 상태 확인
"""

# 이 아래에 직접 작성하세요.
class Quiz:
    def __init__(self, answer):
        self.answer = answer

    def is_correct(self, selected):
        return self.answer == selected

quiz1 = Quiz(1)
quiz2 = Quiz(2)

print(quiz1.is_correct(2))
print(quiz2.is_correct(2))
