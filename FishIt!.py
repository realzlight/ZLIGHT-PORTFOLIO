# IMPORTING
import time, random, os, json

# =============== CLEAN "_" BOX SYSTEM ===============
def b():
	print("_".center(60,"_"))





def box(msg):
    print("\n" + "_".center(60, "_"))
    print("")
    for line in msg.split("\n"):
        print(line.center(60))
    print("")
    print("_".center(60, "_") + "\n")

# TRUESS
infisherman = True
inkohana = False
incrater = False
inclassic = False
inecostier = False
inlost = False
injungle = False

if inkohana == True:
	fishes = [{"name":"Lava Fish", "price":300, "chance": 40}]




# STARTER BANNER
running = False
time.sleep(0.5)
print("_".center(60,"_"))
print("")
print("Fish It!".center(60))
print("")
time.sleep(0.5)
print("1. Play".center(60))
print("")
print("2. Exit".center(60))
print("")
time.sleep(0.5)
print("_".center(60,"_"))
print("")

mainchoice = input(">>> ")

if mainchoice == "1":
    os.system("clear")
    print("")
    print("FishIt:".center(60))
    print("")
    print("Type /help For Help".center(60))
    print("")
    print("FISHERMAN ISLAND".center(60))
    print("")
    print("_".center(60,"_"))
    print("")
    name = input("Enter Your Name: ")
    print("")
    running = True
elif mainchoice == "2":
    running = False
else:
    box("Invalid Choice!")
    running = False


# PLAYER ATTRIBUTe
money = 0
inv = []  
owned_rods = ["Starter Rod"]
selected_rod = "Starter Rod"

# RODS
rods = {
    "Starter Rod": {"price": 0, "boost": 0},
    "Luck Rod": {"price": 2000, "boost": 7},
    "Damascus Rod": {"price": 5000, "boost": 15},
    "MidNight Rod": {"price": 10000, "boost": 25},
    "SteamPunk Rod": {"price": 20000, "boost": 30},
   
    	
}

# FISHES
if infisherman == True:
    fishes = [
    {"name": "Salmon", "chance": 60, "price": 100},
    {"name": "Tuna", "chance": 60, "price": 150},
    {"name": "Yellow Damsel Fish", "chance": 30, "price": 200},
    
    {"name": "Astral Damsel Fish", "chance": 8, "price": 600},
    
    {"name": "Conch Shell", "chance": 45, "price": 50},
    
    {"name": "Troll Fish", "chance" : 20, "price" : 1},
    
]


# =============== INVENTORY ===============
def inventory():
    if len(inv) == 0:
        box("Your inventory is empty!")
    else:
        data = "\n".join([f"{i+1}. {f['name']} — ₹{f['price']}" for i, f in enumerate(inv)])
        box(data)


# =============== ROD INVENTORY ===============
def rod_inventory():
    msg = ""
    for i, rod in enumerate(owned_rods):
        boost = rods[rod]["boost"]
        msg += f"{i+1}. {rod} (Boost: +{boost}%)\n"
    msg += f"\nCurrent Rod: {selected_rod}"
    box(msg)


# =============== SELECT ROD ===============
def select_rod():
    global selected_rod
    choice_raw = input("Select rod number: ").strip()

    if choice_raw == "":
        box("Invalid input! You pressed ENTER.")
        return

    try:
        choice = int(choice_raw)
        if 1 <= choice <= len(owned_rods):
            selected_rod = owned_rods[choice - 1]
            box(f"Rod Selected: {selected_rod}")
        else:
            box("Invalid number!")
    except:
        box("Invalid input!")


# =============== SHOP ===============
def shop():
    global money
    msg = ""

    for rod, data in rods.items():
        msg += f"{rod} — ₹{data['price']} — Boost {data['boost']}%\n"

    box(msg)
    buy = input("Enter rod name to buy: ")

    if buy in rods:
        if buy in owned_rods:
            box("You already own this rod!")
            return

        if money >= rods[buy]["price"]:
            money -= rods[buy]["price"]
            owned_rods.append(buy)
            box(f"You bought: {buy}!")
        else:
            box("Not enough money!")
    else:
        box("Rod not found!")


# =============== SELL SYSTEM ===============
def sell():
    global money

    if len(inv) == 0:
        box("Inventory empty!")
        return

    box("1. Sell One Item\n2. Sell All")
    choice = input("Choose: ")

    if choice == "1":
        inventory()
        try:
            idx = int(input("Enter fish number to sell: ")) - 1
            if 0 <= idx < len(inv):
                money += inv[idx]["price"]
                box(f"Sold {inv[idx]['name']} for ₹{inv[idx]['price']}")
                inv.pop(idx)
            else:
                box("Invalid number!")
        except:
            box("Invalid input!")

    elif choice == "2":
        total = sum(f["price"] for f in inv)
        inv.clear()
        money += total
        box(f"Sold all fish for ₹{total}")

    else:
        box("Invalid choice!")


# =============== FISHING ===============
def fish():
    global selected_rod
    msg = ["Something Is In Your Dart...","Your Rod's String Is Shaking...", "Get Up Something Is Underneath...","Fish Is In Your Dart Maybe..."]
    dura = random.randint(3,5)
    duration = random.randint(1, 10)
    print("")
    b()
    print("")
    print("Fishing...".center(60))
    time.sleep(duration)
    print("")
    rand = random.choice(msg)
    print(rand.center(60))
   
    print("")
    time.sleep(dura)
    print("")
    print("Hurry Up! Pull Fishing Rod, Fast!".center(60))
    print("")
    pull1 = input("Enter 'p' To Pull The Fish >> ")
    pull2 = input("Enter 'p' To Pull The Fish >> ")
    pull3 = input("Enter 'p' To Pull The Fish >> ")
    pull4 = input("Enter 'p' To Pull The Fish >> ")
    pull5 = input("Enter 'p' To Pull The Fish >> ")
    
    
    boost = rods[selected_rod]["boost"]
    weighted = []

    for f in fishes:
        final = f["chance"] + (f["chance"] * boost / 100)
        weighted.extend([f] * int(final))

    caught = random.choice(weighted)
    inv.append(caught)

    box(f"You caught a {caught['name']} worth ₹{caught['price']} %{caught['chance']}!")
b()
# ============== ISLANDS/DAVID ==============
def sail():
    global infisherman, inkohana, incrater, inclassic, inecostier, inlost, injungle, fishes

    print("")
    time.sleep(0.2)
    b()
    print("")
    time.sleep(0.2)
    print("DAVID".center(60))
    print("")
    time.sleep(0.5)
    print("David : Hello There! Iam David I'm A Sailor I'll Take You To Different Islands ")
    print("")
    print("1. FISHERMAN ISLAND\n2. KOHANA VOLCANO\n3. CLASSIC ISLAND\n4. CRATER ISLAND\n5. ANCIENT JUNGLE\n6. ECOSTIER DEPTS\n7. LOST ISLE".center(60))
    time.sleep(0.2)
    print("")
    islandchoice = input("Enter Island No. >>> ")

    # ====================== FISHERMAN ======================
    if islandchoice == "1":
        os.system("clear")
        print("")
        b()
        print("")
        print("Ok Fine We Are Heading To The FISHERMAN ISLAND".center(60))
        print("Its 5s Away From Here!".center(60))
        print("")
        b()
        time.sleep(5)
        os.system("clear")
        print("")
        print("Fish It!".center(60))
        print("")
        print("FISHERMAN ISLAND".center(60))
        print("")
        b()
        print("")

        infisherman = True
        inkohana = False
        incrater = False
        inclassic = False
        inecostier = False
        inlost = False
        injungle = False

        fishes = [
            {"name": "Salmon", "chance": 60, "price": 100},
            {"name": "Tuna", "chance": 60, "price": 150},
            {"name": "Yellow Damsel Fish", "chance": 30, "price": 200},
            {"name": "Astral Damsel Fish", "chance": 8, "price": 600},
            {"name": "Conch Shell", "chance": 45, "price": 50},
            {"name": "Troll Fish", "chance": 20, "price": 1},
        ]

    # ====================== KOHANA VOLCANO ======================

    elif islandchoice == "2":
        os.system("clear")
        print("")
        b()
        print("")
        print("Ok We Are Going To Kohana Volcano! Wait A Bit!".center(60))
        print("")
        b()
        time.sleep(5)
        os.system("clear")
        print("")
        print("Fish It!".center(60))
        print("")
        print("KOHANA VOLCANO".center(60))
        print("")
        b()
        print("")

        infisherman = False
        inkohana = True
        incrater = False
        inclassic = False
        inecostier = False
        inlost = False
        injungle = False

        fishes = [
            {"name": "Lava Fish", "price": 300, "chance": 40}
        ]
        
        
#=================== Crater Island ============
    elif islandchoice == "3":
        os.system("clear")
        print("")
        b()
        print("")
        print("Ok We Are Going To Crater Island! Wait A Bit!".center(60))
        print("")
        b()
        time.sleep(5)
        os.system("clear")
        print("")
        print("Fish It!".center(60))
        print("")
        print("CRATER ISLAND".center(60))
        print("")
        b()
        print("")

        infisherman = False
        inkohana = False
        incrater = True
        inclassic = False
        inecostier = False
        inlost = False
        injungle = False

        fishes = [
            {"name": "CraterFish", "price": 300, "chance": 40}
        ]

#================== Class Island ===================
    elif islandchoice == "4":
        os.system("clear")
        print("")
        b()
        print("")
        print("Ok We Are Going To Classic Island! Wait A Bit!".center(60))
        print("")
        b()
        time.sleep(5)
        os.system("clear")
        print("")
        print("Fish It!".center(60))
        print("")
        print("CLASSIC ISLAND".center(60))
        print("")
        b()
        print("")

        infisherman = False
        inkohana = False
        incrater = False
        inclassic = True
        inecostier = False
        inlost = False
        injungle = False

        fishes = [
            {"name": "Classic Fish", "price": 300, "chance": 40}
        ]
        
        
# =============== Ecoustier ===============

    elif islandchoice == "5":
        os.system("clear")
        print("")
        b()
        print("")
        print("Ok We Are Going To ECOUSTIER ISLAND! Wait A Bit!".center(60))
        print("")
        b()
        time.sleep(5)
        os.system("clear")
        print("")
        print("Fish It!".center(60))
        print("")
        print("ECOUSTIER ISLAND".center(60))
        print("")
        b()
        print("")

        infisherman = False
        inkohana = False
        incrater = False
        inclassic = False
        inecostier = True
        inlost = False
        injungle = False

        fishes = [
            {"name": "Eco Fish", "price": 300, "chance": 40}
        ]



    elif islandchoice == "6":
        os.system("clear")
        print("")
        b()
        print("")
        print("Ok We Are Going To ANCIENT JUNGLE! Wait A Bit!".center(60))
        print("")
        b()
        time.sleep(5)
        os.system("clear")
        print("")
        print("Fish It!".center(60))
        print("")
        print("ANCIENT JUNGLE".center(60))
        print("")
        b()
        print("")

        infisherman = False
        inkohana = False
        incrater = False
        inclassic = False
        inecostier = False
        inlost = False
        injungle = True

        fishes = [
            {"name": "Jungle Fish", "price": 300, "chance": 40}
        ]
        
    elif islandchoice == "7":
        os.system("clear")
        print("")
        b()
        print("")
        print("Ok We Are Going To LOST ISLE! Wait A Bit!".center(60))
        print("")
        b()
        time.sleep(5)
        os.system("clear")
        print("")
        print("Fish It!".center(60))
        print("")
        print("LOST ISLE".center(60))
        print("")
        b()
        print("")

        infisherman = False
        inkohana = True
        incrater = False
        inclassic = False
        inecostier = False
        inlost = True
        injungle = False

        fishes = [
            {"name":"Lost Fish", "price": 300, "chance": 40}
        ]

# =============== SAVE SYSTEM (MOVED UP) ===============
def save_game():
    data = {
        "money": money,
        "inv": inv,
        "owned_rods": owned_rods,
        "selected_rod": selected_rod,
        "islands": {
            "infisherman": infisherman,
            "inkohana": inkohana,
            "incrater": incrater,
            "inclassic": inclassic,
            "inecostier": inecostier,
            "inlost": inlost,
            "injungle": injungle
        }
    }

    with open("save.json", "w") as f:
        json.dump(data, f, indent=4)

    box("Game Saved Successfully!")

def load_game():
    global money, inv, owned_rods, selected_rod
    global infisherman, inkohana, incrater, inclassic, inecostier, inlost, injungle, fishes

    try:
        with open("save.json", "r") as f:
            data = json.load(f)

        money = data["money"]
        inv = data["inv"]
        owned_rods = data["owned_rods"]
        selected_rod = data["selected_rod"]

        # Load islands
        island = data["islands"]
        infisherman = island["infisherman"]
        inkohana = island["inkohana"]
        incrater = island["incrater"]
        inclassic = island["inclassic"]
        inecostier = island["inecostier"]
        inlost = island["inlost"]
        injungle = island["injungle"]

        # Restore correct fish list
        if infisherman:
            fishes = [
                {"name": "Salmon", "chance": 60, "price": 100},
                {"name": "Tuna", "chance": 60, "price": 150},
                {"name": "Yellow Damsel Fish", "chance": 30, "price": 200},
                {"name": "Astral Damsel Fish", "chance": 8, "price": 600},
                {"name": "Conch Shell", "chance": 45, "price": 50},
                {"name": "Troll Fish", "chance": 20, "price": 1},
            ]
        elif inkohana:
            fishes = [{"name": "Lava Fish", "price": 300, "chance": 40}]
        elif incrater:
            fishes = [{"name": "CraterFish", "price": 300, "chance": 40}]
        elif inclassic:
            fishes = [{"name": "Classic Fish", "price": 300, "chance": 40}]
        elif inecostier:
            fishes = [{"name": "Eco Fish", "price": 300, "chance": 40}]
        elif injungle:
            fishes = [{"name": "Jungle Fish", "price": 300, "chance": 40}]
        elif inlost:
            fishes = [{"name": "Lost Fish", "price": 300, "chance": 40}]

        box("Game Loaded Successfully!")

    except FileNotFoundError:
        box("No save file found!")
    except:
        box("Failed to load save!")

# =============== MAIN LOOP ===============
# =============== MAIN LOOP ===============
while running:
    user = input(f"{name}: ").strip().lower()

    if user == "/inv":
        inventory()

    elif user == "/fish":
        fish()

    elif user == "/rods":
        rod_inventory()

    elif user == "/selectrod":
        select_rod()

    elif user == "/shop":
        shop()

    elif user == "/sell":
        sell()

    elif user == "/sail":
        sail()

    elif user == "/save":
        save_game()

    elif user == "/load":
        load_game()

    elif user == "/help":
        box(
            "Available Commands:\n"
            "/inv       - View Inventory\n"
            "/fish      - Go Fishing\n"
            "/rods      - View Owned Rods\n"
            "/selectrod - Select Rod\n"
            "/shop      - Buy New Rods\n"
            "/sell      - Sell Fish\n"
            "/sail      - Travel To Islands\n"
            "/save      - Save Game\n"
            "/load      - Load Game\n"
            "/exit      - Exit Game"
        )

    elif user == "/exit":
        box("Exiting game... Goodbye!")
        running = False

    else:
        box("Invalid command! Type /help for commands.")