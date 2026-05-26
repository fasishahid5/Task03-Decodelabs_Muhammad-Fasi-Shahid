quiz = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["a) Karachi", "b) Islamabad", "c) Lahore"],
        "answer": "b"
    },
    {
        "question": "Which language is used for AI?",
        "options": ["a) Python", "b) HTML", "c) CSS"],
        "answer": "a"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["a) Central Process Unit", "b) Central Processing Unit", "c) Computer Personal Unit"],
        "answer": "b"
    }
]

score = 0

print("🧠 Welcome to DecodeLabs Quiz\n")

for q in quiz:
    print(q["question"])
    for opt in q["options"]:
        print(opt)

    user_ans = input("Your answer: ")

    if user_ans.lower() == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong!\n")

print("Final Score:", score, "/", len(quiz))