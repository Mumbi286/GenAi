def create_study_plan(subject, hours):
    print(f"\n Study Plan for {subject}")
    print(f"Daily Study Time: {hours} hours")

    plan = [
        "Day 1: Learn basics",
        "Day 2: Practice examples",
        "Day 3: Advanced topics",
        "Day 4: Revision",
        "Day 5: Test yourself"
    ]

    for day in plan:
        print(day)

    print("Study plan created successfully!")
