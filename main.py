from quiz import Quiz


def main():
    quiz = Quiz(
        "Python에서 리스트를 만드는 기호는?",
        ["()", "[]", "{}", "<>"],
        2,
    )

    quiz.show()

    print("답은 2!:", quiz.is_correct(2))
    print("답은 1!:", quiz.is_correct(1))


if __name__ == "__main__":
    main()
