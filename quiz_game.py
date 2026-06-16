import random
import time
import json
import os
from datetime import datetime

# ============================================
#   🎯 Python Quiz MCQ Game
#   Author: Student Project
# ============================================

COLORS = {
    "green": "\033[92m",
    "red": "\033[91m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "cyan": "\033[96m",
    "bold": "\033[1m",
    "reset": "\033[0m"
}

def color(text, clr):
    return f"{COLORS.get(clr, '')}{text}{COLORS['reset']}"

# ─── Question Bank ───────────────────────────────────────────────
QUESTIONS = {
    "Python Basics": [
        {
            "question": "Python mein list define karne ka sahi tarika kya hai?",
            "options": ["A) list = (1,2,3)", "B) list = [1,2,3]", "C) list = {1,2,3}", "D) list = <1,2,3>"],
            "answer": "B",
            "explanation": "Python mein list square brackets [ ] se banti hai."
        },
        {
            "question": "Python mein comment likhne ke liye kya use karte hain?",
            "options": ["A) //", "B) /* */", "C) #", "D) --"],
            "answer": "C",
            "explanation": "Python mein single-line comment ke liye # use hota hai."
        },
        {
            "question": "print() function kya karta hai?",
            "options": ["A) Input leta hai", "B) Screen par output dikhata hai", "C) File save karta hai", "D) Variable delete karta hai"],
            "answer": "B",
            "explanation": "print() function screen (console) par text/value dikhata hai."
        },
        {
            "question": "Python mein 'int' ka matlab kya hai?",
            "options": ["A) Text data type", "B) Decimal number", "C) Pura (whole) number", "D) True/False value"],
            "answer": "C",
            "explanation": "int = integer, yani pura number jaise 1, 5, -3 etc."
        },
        {
            "question": "Python mein variable assign karne ka tarika kya hai?",
            "options": ["A) int x = 5", "B) x == 5", "C) x = 5", "D) var x = 5"],
            "answer": "C",
            "explanation": "Python mein sirf x = 5 likhte hain, koi data type declare nahi karna."
        },
    ],
    "Control Flow": [
        {
            "question": "if-else statement kab use karte hain?",
            "options": ["A) Loop chalane ke liye", "B) Condition check karne ke liye", "C) Function banane ke liye", "D) Import karne ke liye"],
            "answer": "B",
            "explanation": "if-else condition check karne ke liye use hoti hai."
        },
        {
            "question": "for loop Python mein kaise likhte hain?",
            "options": ["A) for(i=0; i<5; i++)", "B) for i in range(5):", "C) foreach i in 5:", "D) loop i from 0 to 5:"],
            "answer": "B",
            "explanation": "Python mein for i in range(5): se 0 se 4 tak loop chalta hai."
        },
        {
            "question": "while loop kab rukta hai?",
            "options": ["A) Jab condition True ho", "B) Jab condition False ho jaye", "C) 10 baar baad", "D) Kabhi nahi rukta"],
            "answer": "B",
            "explanation": "while loop tab tak chalta hai jab tak condition True ho, False hone par ruk jata hai."
        },
        {
            "question": "break statement kya karta hai?",
            "options": ["A) Loop ko skip karta hai", "B) Loop ko turant band karta hai", "C) Program ko band karta hai", "D) Next iteration pe jata hai"],
            "answer": "B",
            "explanation": "break loop ko turant todta (exit) karta hai."
        },
        {
            "question": "range(1, 10, 2) kya generate karega?",
            "options": ["A) 1,2,3,4,5,6,7,8,9", "B) 1,3,5,7,9", "C) 2,4,6,8,10", "D) 1,10,2"],
            "answer": "B",
            "explanation": "range(start, stop, step) — 1 se shuru, 10 se pehle, 2 ka step: 1,3,5,7,9"
        },
    ],
    "Functions & OOP": [
        {
            "question": "Python mein function define karne ke liye kya likhte hain?",
            "options": ["A) function myFunc():", "B) def myFunc():", "C) func myFunc():", "D) define myFunc():"],
            "answer": "B",
            "explanation": "Python mein def keyword se function banta hai."
        },
        {
            "question": "Class banane ka tarika kya hai?",
            "options": ["A) class MyClass:", "B) Class MyClass:", "C) create class MyClass:", "D) new MyClass():"],
            "answer": "A",
            "explanation": "class keyword lowercase hota hai: class MyClass:"
        },
        {
            "question": "__init__ method kya hota hai?",
            "options": ["A) Class ka last method", "B) Class ka constructor (initialization)", "C) Class ko delete karta hai", "D) Static method hota hai"],
            "answer": "B",
            "explanation": "__init__ constructor hai jo object bante waqt automatically call hota hai."
        },
        {
            "question": "self parameter kya represent karta hai?",
            "options": ["A) Global variable", "B) Parent class", "C) Class ka current object (instance)", "D) Function ka return value"],
            "answer": "C",
            "explanation": "self current object ko refer karta hai jis par method call ho raha hai."
        },
        {
            "question": "return statement ka kaam kya hai?",
            "options": ["A) Function restart karna", "B) Function se value wapas karna", "C) Loop band karna", "D) Error show karna"],
            "answer": "B",
            "explanation": "return function se calling code ko value wapas bhejta hai."
        },
    ],
    "Data Structures": [
        {
            "question": "Dictionary mein data kaise store hota hai?",
            "options": ["A) Index se", "B) Key-Value pairs mein", "C) Alphabetical order mein", "D) Random order mein"],
            "answer": "B",
            "explanation": "Dictionary mein data key:value format mein hota hai, e.g. {'name': 'Ali'}"
        },
        {
            "question": "Tuple aur List mein kya farq hai?",
            "options": ["A) Koi farq nahi", "B) Tuple mutable hai, List immutable", "C) Tuple immutable hai, List mutable", "D) Tuple sirf numbers store karta hai"],
            "answer": "C",
            "explanation": "Tuple () immutable hai (change nahi hota), List [] mutable hai (change ho sakta hai)."
        },
        {
            "question": "list.append() kya karta hai?",
            "options": ["A) List ka pehla element hatata hai", "B) List ke aakhir mein element add karta hai", "C) List sort karta hai", "D) List copy karta hai"],
            "answer": "B",
            "explanation": "append() list ke end mein nayi value add karta hai."
        },
        {
            "question": "len() function kya return karta hai?",
            "options": ["A) List ka sum", "B) List ka average", "C) List/string ki length (size)", "D) List ka max value"],
            "answer": "C",
            "explanation": "len() list, string, tuple etc. ki length (number of elements) return karta hai."
        },
        {
            "question": "Set data structure ki khasiyat kya hai?",
            "options": ["A) Ordered aur duplicates allowed", "B) Unordered aur no duplicates", "C) Only numbers store karta hai", "D) Key-value pairs"],
            "answer": "B",
            "explanation": "Set unordered hota hai aur duplicate values store nahi karta."
        },
    ]
}

HIGHSCORE_FILE = "highscores.json"

def load_highscores():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as f:
            return json.load(f)
    return []

def save_highscore(name, score, total, category, time_taken):
    scores = load_highscores()
    scores.append({
        "name": name,
        "score": score,
        "total": total,
        "percentage": round((score/total)*100, 1),
        "category": category,
        "time": round(time_taken, 1),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    scores = sorted(scores, key=lambda x: x["percentage"], reverse=True)[:10]
    with open(HIGHSCORE_FILE, "w") as f:
        json.dump(scores, f, indent=2)

def show_highscores():
    scores = load_highscores()
    print(color("\n🏆 TOP 10 HIGH SCORES 🏆", "yellow"))
    print("─" * 60)
    if not scores:
        print(color("Abhi koi score nahi hai. Pehle quiz khelo!", "cyan"))
        return
    for i, s in enumerate(scores, 1):
        medal = ["🥇","🥈","🥉"][i-1] if i <= 3 else f" {i}."
        print(f"{medal} {color(s['name'], 'bold')} | "
              f"{color(str(s['percentage'])+'%', 'green')} | "
              f"{s['score']}/{s['total']} | "
              f"{s['category']} | {s['date']}")
    print("─" * 60)

def show_banner():
    print(color("""
╔══════════════════════════════════════════════════════╗
║          🎯  PYTHON QUIZ MCQ GAME  🎯               ║
║          Apna Python Knowledge Test Karo!            ║
╚══════════════════════════════════════════════════════╝
""", "cyan"))

def get_grade(percentage):
    if percentage >= 90:
        return color("A+ (Shaabaash! Kamaal kar diya! 🌟)", "green")
    elif percentage >= 80:
        return color("A  (Bohat acha! 👍)", "green")
    elif percentage >= 70:
        return color("B  (Acha performance! 😊)", "yellow")
    elif percentage >= 60:
        return color("C  (Pass! Thodi aur mehnat karo 📚)", "yellow")
    elif percentage >= 50:
        return color("D  (Barely pass. Revision karo! 😅)", "yellow")
    else:
        return color("F  (Fail. Dobara try karo! 💪)", "red")

def run_quiz(player_name, category, num_questions, timed_mode):
    questions = QUESTIONS[category].copy()
    random.shuffle(questions)
    questions = questions[:num_questions]

    score = 0
    start_time = time.time()
    results = []

    print(color(f"\n📚 Category: {category} | Questions: {num_questions}", "blue"))
    if timed_mode:
        print(color("⏱️  Timed Mode: 15 seconds per question!", "yellow"))
    print("─" * 55)

    for i, q in enumerate(questions, 1):
        print(color(f"\nQ{i}/{num_questions}: {q['question']}", "bold"))
        for opt in q["options"]:
            print(f"   {opt}")

        q_start = time.time()
        if timed_mode:
            print(color("   ⏰ Aapke paas 15 second hain...", "yellow"))

        while True:
            user_ans = input(color("   Aapka jawab (A/B/C/D): ", "cyan")).strip().upper()
            if user_ans in ["A", "B", "C", "D"]:
                break
            print(color("   ❌ Sirf A, B, C ya D likhein!", "red"))

        q_time = time.time() - q_start

        if timed_mode and q_time > 15:
            print(color("   ⏰ Time khatam! Yeh question skip ho gaya.", "red"))
            results.append({"q": q["question"], "correct": False, "your_ans": "TIMEOUT", "right_ans": q["answer"]})
            continue

        if user_ans == q["answer"]:
            print(color("   ✅ Bilkul sahi! Shabaash!", "green"))
            score += 1
            results.append({"q": q["question"], "correct": True})
        else:
            print(color(f"   ❌ Galat! Sahi jawab: {q['answer']}", "red"))
            print(color(f"   💡 {q['explanation']}", "yellow"))
            results.append({"q": q["question"], "correct": False, "your_ans": user_ans, "right_ans": q["answer"]})

    total_time = time.time() - start_time
    percentage = (score / num_questions) * 100

    print(color("\n" + "═" * 55, "cyan"))
    print(color("           📊 QUIZ RESULT 📊", "bold"))
    print(color("═" * 55, "cyan"))
    print(f"  👤 Player  : {color(player_name, 'bold')}")
    print(f"  📚 Category: {category}")
    print(f"  ✅ Score   : {color(f'{score}/{num_questions}', 'green')}")
    print(f"  📈 Marks   : {color(f'{percentage:.1f}%', 'yellow')}")
    print(f"  ⏱️  Time    : {total_time:.1f} seconds")
    print(f"  🎓 Grade   : {get_grade(percentage)}")
    print(color("═" * 55, "cyan"))

    wrong = [r for r in results if not r["correct"]]
    if wrong:
        print(color(f"\n❌ Galat jawab ({len(wrong)}):", "red"))
        for r in wrong:
            print(f"  • {r['q'][:50]}...")

    save_highscore(player_name, score, num_questions, category, total_time)
    print(color("\n🏆 Score save ho gaya!", "green"))

def main():
    show_banner()

    while True:
        print(color("\n📋 MAIN MENU", "bold"))
        print("  1. Quiz Khelo")
        print("  2. High Scores Dekho")
        print("  3. Quit")

        choice = input(color("\nAapka choice (1-3): ", "cyan")).strip()

        if choice == "3":
            print(color("\n👋 Shukriya! Fikri rehna, Python seekhte raho! 🐍\n", "yellow"))
            break

        elif choice == "2":
            show_highscores()

        elif choice == "1":
            player_name = input(color("\n👤 Apna naam likhein: ", "cyan")).strip()
            if not player_name:
                player_name = "Student"

            print(color("\n📚 Category chunein:", "bold"))
            categories = list(QUESTIONS.keys())
            for i, cat in enumerate(categories, 1):
                print(f"  {i}. {cat} ({len(QUESTIONS[cat])} questions)")
            print(f"  {len(categories)+1}. Random Mix (Sab categories se)")

            while True:
                cat_choice = input(color("Category number: ", "cyan")).strip()
                if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories)+1:
                    break
                print(color("Galat choice! Dobara try karein.", "red"))

            if int(cat_choice) == len(categories)+1:
                all_q = []
                for qs in QUESTIONS.values():
                    all_q.extend(qs)
                selected_cat = "Random Mix"
                max_q = min(len(all_q), 10)
                QUESTIONS["Random Mix"] = all_q
            else:
                selected_cat = categories[int(cat_choice)-1]
                max_q = len(QUESTIONS[selected_cat])

            print(color(f"\nKitne questions chahiye? (1-{max_q})", "bold"))
            while True:
                num_q = input(color("Questions ki tadaad: ", "cyan")).strip()
                if num_q.isdigit() and 1 <= int(num_q) <= max_q:
                    num_q = int(num_q)
                    break
                print(color(f"1 aur {max_q} ke beech number likhein!", "red"))

            timed = input(color("\n⏱️  Timed mode ON karna hai? (y/n): ", "cyan")).strip().lower() == "y"

            run_quiz(player_name, selected_cat, num_q, timed)

            if "Random Mix" in QUESTIONS:
                del QUESTIONS["Random Mix"]
        else:
            print(color("❌ Galat choice! 1, 2 ya 3 likhein.", "red"))

if __name__ == "__main__":
    main()
