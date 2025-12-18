from study_planner import create_study_plan
from quiz_engine import start_quiz

def menu():
    print("\n AI Personal Study Buddy")
    print("1. Create Study Plan")
    print("2. Take a Quiz")
    print("3. View Progress")
    print("4. Get Motivation")
    print("5. Exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        subject = input("What subject are you studying? ")
        hours = input("How many hours per day can you study? ")
        create_study_plan(subject, hours)

    elif choice == "2":
        start_quiz()

    elif choice == "3":
        view_progress()

    elif choice == "4":
        motivate_user()

    elif choice == "5":
        print("Goodbye! Keep learning ")
        break

    else:
        print("Invalid choice. Try again.")
