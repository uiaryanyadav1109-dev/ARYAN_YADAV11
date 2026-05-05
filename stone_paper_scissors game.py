import random
#USER NAME

user_name = input("Enter Your Name:")
print("USER NAME IS:", user_name)

#OPTIONS 

options = ["stone", "scissors", "paper"]
rounds = int(input("FOR HOW MANY ROUNDS YOU WANT TO PLAY:"))
user_score = 0
comp_score = 0

#NUMBERS OF ROUNDS

for round_num in range(1, rounds + 1):
    print(f"\n--- Round {round_num} ---")
    
    # VALID INPUT LOOP
    
    while True:
        user_option = input("ENTER YOUR CHOICE (STONE/SCISSORS/PAPER): ").lower()
        if user_option in options:
            print(user_name,"HAS CHOSEN:", user_option.upper())
            break
        else:
            print("WRONG OPTION! PLEASE ENTER AGAIN.")
    
    #COMPUTER OPTIONS

    comp_option = random.choice(options)
    print("COMPUTER HAS CHOSEN:", comp_option.upper())
    
    # WIN CONDITIONS
    
    if (
        (user_option == "stone" and comp_option == "scissors") or
        (user_option == "paper" and comp_option == "stone") or
        (user_option == "scissors" and comp_option == "paper")
    ):
        print(user_option.upper(), ":", user_name, "HAS WON!!!")
        user_score += 1
    
    elif (
        (comp_option == "stone" and user_option == "scissors") or
        (comp_option == "paper" and user_option == "stone") or
        (comp_option == "scissors" and user_option == "paper")
    ):
        print(comp_option.upper(), ":", "COMPUTER HAS WON!!!")
        comp_score += 1
    
    else:
        print("MATCH DRAWN")

# FINAL RESULT

print("\n=== FINAL RESULT ===")
print(f"Score -> user_score: {user_score}, comp_score: {comp_score}")

if user_score > comp_score:
    print(user_name,"wins the game!")
elif comp_score > user_score:
    print("Computer wins the game!")
else:
    print("It's a tie!")