import time
import threading
import random

#-------------- Leveling System ----------------#
lvl = 1
lvlpoint = 0
maxpoint = 15 # points needed to level up

def add_level_point(points=1):
    global lvl, lvlpoint, maxpoint
    
    lvlpoint += points

    # Auto Level Up (Overflow System)
    while lvlpoint >= maxpoint:
        lvl += 1
        lvlpoint -= maxpoint
        print("\n🎉 LEVEL UP!!! 🎉")
        print(f"New Level: {lvl}")
        print("_".center(60, "_"))

#-------------- Money System ----------------#
money = 100
key = "zlight"   # admin key

#-------------- Starter Banner ----------------#
time.sleep(0.5)
print("Welcome To Valiant City".center(63))
time.sleep(0.5)
print("Type /help To Get Help If You Are New ".center(63))
time.sleep(0.5)
print("_".center(60, "_"))
time.sleep(0.5)

#-------------- Get Player Name ----------------#
print("")
time.sleep(0.5)
name = input(">>> Enter Your Name : ")
time.sleep(0.5)
print("_".center(60, "_"))
print("")

#-------------- Hunger System ----------------#
hunger_max = 15
hunger_points = 9
running = True

def get_hunger_bar():
    return "🍗" * hunger_points

def hunger_loop():
    global hunger_points, running
    while running:
        time.sleep(30)
        hunger_points -= 1

        if hunger_points <= 1:
            print("\n" + "_"*60)
            print("⚠️ Warning: Last hunger point! Eat now!")
            print("_"*60)

        if hunger_points <= 0:
            hunger_points = 0
            print("\nYour hunger dropped to 0! Game Over!")
            running = False
            break

hunger_thread = threading.Thread(target=hunger_loop, daemon=True)
hunger_thread.start()

#-------------- Quiz Questions ----------------#
quiz_questions = [
    ("What's the capital of France?", "paris"),
    ("2 + 2 = ?", "4"),
    ("Which planet is known as the Red Planet?", "mars"),
    ("12 x 2 = ?", "24"),
    ("What's the largest ocean on Earth?", "pacific")
]

#-------------- Custom Quiz ----------------#
custom_quiz = [
    ("Your custom question 1?", "answer1"),
    ("Your custom question 2?", "answer2"),
]

entry_fee = 10
reward = 50

#-------------- Stylish Boxes ----------------#
def stylish_question(text):
    print("")
    print("_".center(60, "_"))
    print("")
    print(text)
    print("")
    print("_".center(60, "_"))
    print("")

def ask_question(q, ans, timeout=10):
    stylish_question(q)
    timer = threading.Timer(timeout, lambda: print("\nTime's up!"))
    timer.start()
    user_ans = input("Your answer: ").strip()
    timer.cancel()
    return user_ans.lower() == ans.lower()

def stylish_box(text):
    print("")
    print("_".center(60, "_"))
    print("")
    print(text)
    print("")
    print("_".center(60, "_"))
    print("")

#-------------- Regular Quiz ----------------#
def run_regular_quiz():
    global money
    print("\n--- Regular Quiz ---")

    pay = input(f"Entry fee: {entry_fee} coins. Pay? (yes/no): ").lower()
    if pay != "yes":
        print("OK, maybe later!")
        return

    if money < entry_fee:
        print("Not enough money!")
        return

    money -= entry_fee
    print("Fee paid! Starting quiz...\n")

    correct = 0
    questions = quiz_questions.copy()

    for _ in range(5):
        if not questions:
            break
        q, a = random.choice(questions)
        questions.remove((q, a))
        if ask_question(q, a):
            correct += 1

    print(f"You got {correct}/5 correct.")

    if correct >= 3:
        money += reward
        print(f"You win {reward} coins! 🎉")
        print("")
        print("You Got One lvl Point!! +1")
        print("")
        print("_".center(60, "_"))
        add_level_point(1)
    else:
        print("Better luck next time!")

#-------------- Custom Quiz ----------------#
def run_custom_quiz():
    global money
    print("\n--- Custom Quiz ---")
    print("This quiz uses your custom questions!")
    print("")

    pay = input(f"Entry fee: {entry_fee} coins. Pay? (yes/no): ").lower()
    if pay != "yes":
        print("OK, maybe later!")
        return

    if money < entry_fee:
        print("Not enough money!")
        return

    money -= entry_fee
    print("Fee paid! Starting custom quiz...\n")

    correct = 0
    for q, a in custom_quiz:
        if ask_question(q, a):
            correct += 1

    print(f"You got {correct}/{len(custom_quiz)} correct.")

    if correct >= len(custom_quiz) // 2:
        money += reward
        print(f"You win {reward} coins! 🎉")
        add_level_point(1)
    else:
        print("Better luck next time!")

#-------------- Head & Tail Game ----------------#
def head_tail():
    global money

    stylish_box("Do You Wanna Play Head & Tail? (yes/no)")
    play = input(">>> ").lower()

    if play != "yes":
        print("Okay, maybe later!")
        return

    stylish_box(f"Your Balance: {money}\nEnter Bet Amount:")
    try:
        bet = int(input(">>> "))
    except:
        print("Invalid amount!")
        return

    if bet > money:
        print("You don't have enough money!")
        return
    if bet <= 0:
        print("Bet must be more than 0!")
        return

    stylish_box("Choose:\nH = Head\nT = Tail")
    choice = input(">>> ").lower()

    if choice not in ["h", "t"]:
        print("Invalid choice!")
        return

    result = random.choice(["h", "t"])

    stylish_box(f"Result: {'Head' if result == 'h' else 'Tail'}")

    if choice == result:
        money += bet
        print(f"You Won! +{bet} coins 🎉")
    else:
        money -= bet
        print(f"You Lost! -{bet} coins 😢")

    stylish_box(f"New Balance: {money}")


def get_level_bar():
    bar_length = 20  # total bar size
    filled = int((lvlpoint / maxpoint) * bar_length)
    empty = bar_length - filled
    return "[" + "█" * filled + "-" * empty + f"] {lvlpoint}/{maxpoint}"




#-------------- Main Command Loop ----------------#
while running:
    print("")
    user = input(f"{name}: ")
    
    
    #-----------------LVL REWARDS------------
   
    
    
    
    
    
    
    

    # -------- ADMIN PANEL -------- #
    if user.startswith("/admin"):
        print("")
        print("_".center(60, "_"))
        print("")
        print("Admin Panel".center(60, "-"))
        print("")

        passcheck = input(">>> Key : ").lower()
        print("")

        if passcheck == key:
            print("✔ Access Granted")
            print("_".center(60, "_"))
            moneyinput = int(input(">>> Enter Money Amount To Add : "))
            money += moneyinput
            print("")
            print(f"💰 {moneyinput} Coins Added!")
            print("_".center(60, "_"))
        else:
            print("❌ Invalid Key!")
            print("_".center(60, "_"))
        continue

    # -------- HELP -------- #
    if user.startswith("/help"):
        print("_".center(60, "_"))
        print("HELP".center(63))
        print("""
This is the help for Valiant City.  
• /bal = check balance  
• /shop = shop  
• /food = eat food  
• /quiz = play quiz  
• /ht = head & tail  
• /hunger = hunger status  
• /lvl = check level  
• /cmd = list commands  
""")
        print("_".center(60, "_"))

    elif user.startswith("/hunger"):
        print("_".center(60, "_"))
        print("Hunger:", get_hunger_bar(), f"({hunger_points}/{hunger_max})")
        print("_".center(60, "_"))

    elif user.startswith("/quit"):
        print("Bye!!!")
        print("_".center(60, "_"))
        running = False

    elif user.startswith("/bal"):
        print("_".center(60, "_"))
        print("Current Balance: $", money)
        print("_".center(60, "_"))

    elif user.startswith("/cmd"):
        print("_".center(60, "_"))
        print("Commands:")
        print("/shop\n/bal\n/food\n/hunger\n/ht\n/quiz\n/lvl\n/cmd")
        print("_".center(60, "_"))

    elif user.startswith("/quiz"):
        print("_".center(60, "_"))
        print("Select Quiz Type".center(60))
        print("_".center(60, "_"))
        print("1 → Regular Quiz\n2 → Custom Quiz\n")
        choice = input("Enter 1 or 2: ")

        if choice == "1":
            run_regular_quiz()
        elif choice == "2":
            run_custom_quiz()
        else:
            print("Invalid choice!")

    elif user.startswith("/ht"):
        head_tail()

    elif user.startswith("/food"):
        print("")
        time.sleep(0.3)
        print("_".center(60, "_"))
        print("FOOD MENU".center(63))
        print("")
        print("Current Balance : ", money, "$")
        print("")
        print("1. French Fries - 50$ (+1 hunger)")
        print("2. Burger       - 100$ (+3 hunger)")
        print("3. Pizza        - 300$ (+2 hunger)")
        print("4. HamBurger    - 500$ (+5 hunger)")
        print("")

        try:
            foodinput = int(input("Enter Food Number To Purchase : "))
        except:
            print("Invalid choice!")
            continue

        print("_".center(60, "_"))

        food_restore = 0
        cost = 0
        name_food = ""

        if foodinput == 1:
            cost = 50
            food_restore = 1
            name_food = "French Fries"

        elif foodinput == 2:
            cost = 100
            food_restore = 3
            name_food = "Burger"

        elif foodinput == 3:
            cost = 300
            food_restore = 2
            name_food = "Pizza"

        elif foodinput == 4:
            cost = 500
            food_restore = 5
            name_food = "HamBurger"

        else:
            print("Invalid food number!")
            continue

        if money < cost:
            print("Not enough money!")
            continue

        money -= cost
        hunger_points = min(hunger_points + food_restore, hunger_max)

        print("")
        print(f"Purchased {name_food} for {cost}$")
        print(f"Restored +{food_restore} hunger point(s)")
        print(f"Current Hunger: {get_hunger_bar()}")
        print("Current Balance : ", money)
        print("_".center(60, "_"))

    # -------- LEVEL COMMAND -------- #
    elif user.startswith("/lvl"):
        print("")
        print("_".center(60, "_"))
        print("")
        print("Level Stats".center(63))
        print("")
        
        print(f"Level : {lvl}")
        print("")
        print(get_level_bar())
        print("")
        print("_".center(60, "_"))
    
    elif user.startswith("/shop"):
        print("")
        print("_".center(60, "_"))
        print("")
        print("SHOP".center(63))
        print("")
        print("1. LVL Shard I  - 100$ (+1 lvlpoint)")
        print("2. LVL Shard II - 200$ (+2 lvlpoint)")
        print("")
        print("Current Balance :", money)
        print("")

        try:
            shopinput = int(input("Enter Number To Buy : "))
        except:
            print("Invalid Choice !!")
            continue

        print("")

        # ---------- SHARD I ----------
        if shopinput == 1:
            if money < 100:
                print("Not Enough Money!")
                print("_".center(60, "_"))
                continue

            money -= 100
            add_level_point(1)
            print("You purchased LVL Shard I for 100$ and used it!")
            print("+1 Level Point")
            print("_".center(60, "_"))
            print("")

        # ---------- SHARD II ----------
        elif shopinput == 2:
            if money < 200:
                print("Not Enough Money!")
                print("_".center(60, "_"))
                continue

            money -= 200
            add_level_point(2)
            print("You purchased LVL Shard II for 200$ and used it!")
            print("+2 Level Points")
            print("_".center(60, "_"))
            print("")

        # ---------- INVALID OPTION ----------
        else:
            print("Invalid Choice !!")
            print("_".center(60, "_"))
            continue