"""
[실습 02] 인스턴스 생성하기 (create an instance)

목표:
- 클래스와 인스턴스(instance)의 차이를 확인한다.

직접 작성:
1. 빈 `Quiz` 클래스를 정의한다.
2. `Quiz()`를 호출해 서로 다른 객체 두 개를 만든다.
3. 두 객체를 출력하고 `quiz1 is quiz2`도 출력한다.

통과 조건:
- 두 객체가 모두 `Quiz`의 인스턴스다.
- `assert quiz1 is not quiz2`가 통과한다.

커밋 예: Study: Quiz 인스턴스 생성 연습
"""

# 이 아래에 직접 작성하세요.
class Quiz:
    pass

quiz1 = Quiz()
quiz2 = Quiz()

print(quiz1)
print(quiz2)
print(quiz1 is quiz2)
assert quiz1 is not quiz2 # 지금은 True지만, False면 AssertionError를 내놓는다고 함.
