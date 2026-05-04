import time
# START OF THE PROGRAM...
print("WELCOME TO MY COMPUTER QUIZ GAME:)")
print("RULES:\n A.RULES ARE SIMPLE THERE ARE THREE LEVELS OF THIS QUIZ GAME\n1.BEGINNER\n2.INTERMEDIATE\n3.ADVANCED")
print("B.There are total of 30 questions, after each 10 questions difficulty of the questions will be increased")
print("C.SCORE/POINTS: THE QUIZ IS OF 100 POINTS, YOU HAVE TO SCORE AT LEAST 33 POINTS TO PASS THE QUIZ")

# GAME START
play_game = input("Do you want to play? (YES/NO) = ")
if play_game.lower() == "yes":
    print("OKAY!!, LET'S PLAY THE GAME:\n3...2...1...\nSTART!...")
else:
    print("OKAY!, NO PROBLEM, THANKS FOR COMING UP TO THIS...")
#INSTRUCTIONS
print("note: Enter all the answers in small letters.")
print("You have 60 seconds for each question.")
print("The Marks/Points are distributed into 3 sections\n1.BEGINNER (2 points each)\n2.INTERMEDIATE (3 points each)\n3. ADVANCED (5 points each)")
#QUESTIONS 
questions = [
     # BEGINNER (2 points each)
    ("What does CPU stand for?", "central processing unit", 2),
    ("What does RAM stand for?", "random access memory", 2),
    ("What does ROM stand for?", "read only memory", 2),
    ("What does USB stand for?", "universal serial bus", 2),
    ("What does UPS stand for?", "uninterruptible power supply", 2),
    ("What is the full form of HTML?", "hypertext markup language", 2),
    ("What is a keyboard used for?", "for typing and giving commands", 2),
    ("What is a mouse used for?", "control and navigate the computer", 2),
    ("What is a monitor used for?", "shows text, images, and videos", 2),
    ("What is the use of a printer?", "used to print documents and pictures on paper", 2),

    # INTERMEDIATE (3 points each)
    ("What is IP address?", "internet protocol address", 3),
    ("What is HTTP?", "hypertext transfer protocol", 3),
    ("What is database?", "collection of data", 3),
    ("What is browser?", "software to access internet", 3),
    ("What is binary language?", "0 and 1", 3),
    ("What is RAM used for?", "temporary memory", 3),
    ("What is operating system?", "software that manages hardware", 3),
    ("What is cloud computing?", "internet based computing", 3),
    ("What is algorithm?", "step by step solution", 3),
    ("What is CPU cache?", "faster memory", 3),

    # ADVANCED (5 points each)
    ("What is AI?", "machines that simulate human intelligence", 5),
    ("What is machine learning?", "systems that learn from data", 5),
    ("What is blockchain?", "distributed digital ledger", 5),
    ("What is encryption?", "data security method", 5),
    ("What is API?", "application programming interface", 5),
    ("What is compiler?", "translates code to machine language", 5),
    ("What is neural network?", "model inspired by brain", 5),
    ("What is cybersecurity?", "protection of systems", 5),
    ("What is big data?", "large complex datasets", 5),
    ("What is quantum computing?", "computing using quantum mechanics", 5),

]
total_score = 0
#ANSWERS CHECKING
for index, (question, correct_answer, points) in enumerate(questions, start=1):
    print(f"QUESTION {index}:{question}")
    start_time = time.time()
    user_answer = input("ENTER YOUR ANSWER HERE---->: ").lower().strip()
    end_time = time.time()

    time_taken = end_time - start_time
# SCORE CALCULATION
    if time_taken > 60:
        print("Time's up! No points awarded.")
        continue

    if user_answer == correct_answer:
        print("CORRECT!!")
        total_score += points
    else:
        print(f"INCORRECT!!, CORRECT ANSWER IS: {correct_answer}")
        total_score -= 0.25
#COMPLETION OF THE QUIZ
print("CONGRATULATIONS!!!\nYOU HAVE CROSSED ALL LEVELS/STAGES OF THE QUIZ...")
print("\nQUIZ COMPLETED!")
print("Your Final Score:", total_score)

# RESULT
if total_score == 100:
    print("Excellent!")
elif total_score >= 90:
    print("Outstanding!")
elif total_score >=70:
    print("Very Good!")
elif total_score >= 50:
    print("Good!")
elif total_score >=33:
    print("Pass!")
else:
    print("FAIL!")