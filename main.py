from quiz_game import QuizGame


def main():
    game = QuizGame()

    print("기본 퀴즈 수:", len(game.quizzes))
    print("최고 점수:", game.best_score)

    for number, quiz in enumerate(game.quizzes, start=1):
        print(f"\n문제 {number}")
        quiz.show()


if __name__ == "__main__":
    main()
