def start_quiz():
    score = 0

    print("\n Quick Quiz")

    questions = {
        "What does CPU stand for? ": "central processing unit",
        "What language is used for AI? ": "python"
    }

    for q, a in questions.items():
        answer = input(q).lower()
        if answer == a:
            print("Correct ")
            score += 1
        else:
            print("Wrong")

    print(f"Your score: {score}/{len(questions)}")
