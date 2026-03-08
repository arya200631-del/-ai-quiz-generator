import random

# ─────────────────────────────────────────────
#  QUESTION BANK
# ─────────────────────────────────────────────

QUESTIONS = {
    "ai": [
        {
            "question": "What does AI stand for?",
            "options": {"a": "Automated Input", "b": "Artificial Intelligence", "c": "Analog Interface", "d": "Applied Integration"},
            "answer": "b",
            "explanation": "AI stands for Artificial Intelligence — machines simulating human thinking."
        },
        {
            "question": "Which of these is a popular AI assistant?",
            "options": {"a": "Photoshop", "b": "Excel", "c": "ChatGPT", "d": "Notepad"},
            "answer": "c",
            "explanation": "ChatGPT is an AI chatbot made by OpenAI."
        },
        {
            "question": "What is Machine Learning?",
            "options": {"a": "Teaching machines to repair themselves", "b": "A branch of AI where machines learn from data", "c": "Programming machines manually", "d": "Building robots"},
            "answer": "b",
            "explanation": "Machine Learning lets computers improve by learning patterns from data."
        },
        {
            "question": "Which language is most commonly used in AI development?",
            "options": {"a": "Java", "b": "C++", "c": "Python", "d": "HTML"},
            "answer": "c",
            "explanation": "Python is the most popular language for AI and data science."
        },
        {
            "question": "What is a neural network inspired by?",
            "options": {"a": "Computer circuits", "b": "The human brain", "c": "DNA strands", "d": "Solar panels"},
            "answer": "b",
            "explanation": "Neural networks mimic how neurons in the human brain connect and communicate."
        },
        {
            "question": "What does NLP stand for in AI?",
            "options": {"a": "Network Layer Protocol", "b": "Natural Language Processing", "c": "Numeric Logic Programming", "d": "Neural Link Processor"},
            "answer": "b",
            "explanation": "NLP helps computers understand and generate human language."
        },
        {
            "question": "Which of these is an example of AI in everyday life?",
            "options": {"a": "A toaster", "b": "A ceiling fan", "c": "A spam email filter", "d": "A USB cable"},
            "answer": "c",
            "explanation": "Spam filters use AI to detect and block unwanted emails."
        },
    ],

    "python": [
        {
            "question": "What is Python?",
            "options": {"a": "A snake", "b": "A high-level programming language", "c": "A database", "d": "An operating system"},
            "answer": "b",
            "explanation": "Python is a beginner-friendly, high-level programming language."
        },
        {
            "question": "How do you print text in Python?",
            "options": {"a": "echo('Hello')", "b": "console.log('Hello')", "c": "print('Hello')", "d": "printf('Hello')"},
            "answer": "c",
            "explanation": "print() is the built-in function for displaying output in Python."
        },
        {
            "question": "Which symbol is used for comments in Python?",
            "options": {"a": "//", "b": "/*", "c": "--", "d": "#"},
            "answer": "d",
            "explanation": "The # symbol starts a single-line comment in Python."
        },
        {
            "question": "What does 'len()' do in Python?",
            "options": {"a": "Deletes a list", "b": "Returns the length of an object", "c": "Loops through items", "d": "Adds numbers"},
            "answer": "b",
            "explanation": "len() returns the number of items in a string, list, or other object."
        },
        {
            "question": "How do you create a list in Python?",
            "options": {"a": "list = (1, 2, 3)", "b": "list = {1, 2, 3}", "c": "list = [1, 2, 3]", "d": "list = <1, 2, 3>"},
            "answer": "c",
            "explanation": "Lists in Python are created using square brackets []."
        },
        {
            "question": "What keyword starts a function in Python?",
            "options": {"a": "function", "b": "func", "c": "def", "d": "define"},
            "answer": "c",
            "explanation": "The 'def' keyword is used to define a function in Python."
        },
        {
            "question": "What does '==' do in Python?",
            "options": {"a": "Assigns a value", "b": "Checks if two values are equal", "c": "Adds two numbers", "d": "Divides two numbers"},
            "answer": "b",
            "explanation": "'==' is the equality operator — it compares two values."
        },
    ],

    "general knowledge": [
        {
            "question": "What is the capital of France?",
            "options": {"a": "Berlin", "b": "Madrid", "c": "Paris", "d": "Rome"},
            "answer": "c",
            "explanation": "Paris is the capital and largest city of France."
        },
        {
            "question": "How many planets are in our solar system?",
            "options": {"a": "7", "b": "8", "c": "9", "d": "10"},
            "answer": "b",
            "explanation": "There are 8 planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune."
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": {"a": "Atlantic", "b": "Indian", "c": "Arctic", "d": "Pacific"},
            "answer": "d",
            "explanation": "The Pacific Ocean is the largest, covering more than 30% of Earth's surface."
        },
        {
            "question": "Who invented the telephone?",
            "options": {"a": "Thomas Edison", "b": "Alexander Graham Bell", "c": "Nikola Tesla", "d": "Albert Einstein"},
            "answer": "b",
            "explanation": "Alexander Graham Bell is credited with inventing the telephone in 1876."
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": {"a": "WA", "b": "HO", "c": "H2O", "d": "OX"},
            "answer": "c",
            "explanation": "Water is made of 2 hydrogen atoms and 1 oxygen atom — H2O."
        },
        {
            "question": "How many continents are there on Earth?",
            "options": {"a": "5", "b": "6", "c": "7", "d": "8"},
            "answer": "c",
            "explanation": "There are 7 continents: Africa, Antarctica, Asia, Australia, Europe, North America, South America."
        },
        {
            "question": "What is the fastest animal on land?",
            "options": {"a": "Lion", "b": "Horse", "c": "Cheetah", "d": "Leopard"},
            "answer": "c",
            "explanation": "The cheetah can reach speeds of up to 120 km/h (75 mph)."
        },
    ],
}

# ─────────────────────────────────────────────
#  DISPLAY HELPERS
# ─────────────────────────────────────────────

DIVIDER  = "-" * 50
BOLD_DIV = "=" * 50

def banner():
    print("\n" + BOLD_DIV)
    print("     AI STUDY QUIZ GENERATOR")
    print("   Sharpen your knowledge, one question at a time!")
    print(BOLD_DIV)

def show_topics():
    print("\nAvailable Topics:")
    print("  1. Artificial Intelligence (AI)")
    print("  2. Python")
    print("  3. General Knowledge")
    print(DIVIDER)

def pick_topic():
    show_topics()
    while True:
        raw = input("Enter topic: ").strip().lower()
        # Accept number shortcuts
        mapping = {"1": "ai", "2": "python", "3": "general knowledge"}
        topic = mapping.get(raw, raw)
        if topic in QUESTIONS:
            return topic
        print(f"  '{raw}' not found. Try: AI, Python, or General Knowledge\n")

def ask_num_questions(max_q):
    while True:
        try:
            n = int(input(f"How many questions? (1–{max_q}): "))
            if 1 <= n <= max_q:
                return n
            print(f"    Please enter a number between 1 and {max_q}.")
        except ValueError:
            print("    Please enter a valid number.")

# ─────────────────────────────────────────────
#  QUIZ ENGINE
# ─────────────────────────────────────────────

def run_quiz(topic, num_questions):
    pool = random.sample(QUESTIONS[topic], num_questions)
    score = 0
    wrong_ones = []

    print(f"\n{BOLD_DIV}")
    print(f"   Topic : {topic.title()}   |   Questions : {num_questions}")
    print(BOLD_DIV)

    for i, q in enumerate(pool, start=1):
        print(f"\nQ{i}. {q['question']}")
        for key, val in q["options"].items():
            print(f"    {key}) {val}")

        # Get answer
        while True:
            ans = input("Your answer (a/b/c/d): ").strip().lower()
            if ans in ("a", "b", "c", "d"):
                break
            print("    Please enter a, b, c, or d.")

        if ans == q["answer"]:
            print("    Correct!")
            score += 1
        else:
            correct_text = q["options"][q["answer"]]
            print(f"    Wrong! Correct answer: {q['answer']}) {correct_text}")
            wrong_ones.append(q)

        print(f"    {q['explanation']}")
        print(DIVIDER)

    return score, num_questions, wrong_ones

# ─────────────────────────────────────────────
#  RESULTS
# ─────────────────────────────────────────────

def show_results(score, total, wrong_ones):
    pct = round((score / total) * 100)
    print(f"\n{BOLD_DIV}")
    print(f"     RESULTS")
    print(BOLD_DIV)
    print(f"   Score   : {score} / {total}")
    print(f"   Percent : {pct}%")

    if pct == 100:
        print("   Rating  :  Perfect Score! Outstanding!")
    elif pct >= 80:
        print("   Rating  :  Excellent work!")
    elif pct >= 60:
        print("   Rating  :  Well done, keep it up!")
    elif pct >= 40:
        print("   Rating  :  Keep studying, you'll get there!")
    else:
        print("   Rating  :  Don't give up — practice makes perfect!")

    if wrong_ones:
        print(f"\n   Questions to review ({len(wrong_ones)}):")
        for q in wrong_ones:
            correct = q["options"][q["answer"]]
            print(f"   • {q['question']}")
            print(f"     Answer: {q['answer']}) {correct}")
    print(BOLD_DIV)

# ─────────────────────────────────────────────
#  MAIN LOOP
# ─────────────────────────────────────────────

def main():
    banner()
    while True:
        topic = pick_topic()
        max_q = len(QUESTIONS[topic])
        num   = ask_num_questions(max_q)

        score, total, wrong = run_quiz(topic, num)
        show_results(score, total, wrong)

        print("\nWhat would you like to do?")
        print("  1. Play again (same topic)")
        print("  2. Choose a new topic")
        print("  3. Quit")
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            continue
        elif choice == "2":
            print()
            continue
        else:
            print("\n  Thanks for studying! Keep learning every day.\n")
            break

if __name__ == "__main__":
    main()
