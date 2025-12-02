# IMPORTING
import time, random, os

# =============== CLEAN "_" BOX SYSTEM ===============
def box(msg):
    print("\n" + "_".center(60, "_"))
    print("")
    for line in msg.split("\n"):
        print(line.center(60))
    print("")
    print("_".center(60, "_") + "\n")


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


# PLAYER ATTRIBUTES
money = 100
inv = []  
owned_rods = ["Wooden Rod"]
selected_rod = "Wooden Rod"

# RODS
rods = {
    "Wooden Rod": {"price": 0, "boost": 0},
    "Iron Rod": {"price": 200, "boost": 10},
    "Golden Rod": {"price": 500, "boost": 25},
    "Diamond Rod": {"price": 1500, "boost": 50}
}

# FISHES
fishes = [
    {"name": "Salmon", "chance": 60, "price": 100},
    {"name": "Tuna", "chance": 60, "price": 150},
    {"name": "Tropical Fish", "chance": 30, "price": 200},
    {"name": "Shark", "chance": 8, "price": 600},
    {"name": "Whale", "chance": 2, "price": 1500},
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

    duration = random.randint(1, 10)
    box("Fishing...")
    time.sleep(duration)

    boost = rods[selected_rod]["boost"]
    weighted = []

    for f in fishes:
        final = f["chance"] + (f["chance"] * boost / 100)
        weighted.extend([f] * int(final))

    caught = random.choice(weighted)
    inv.append(caught)

    box(f"You caught a {caught['name']} worth ₹{caught['price']}!")


# =============== MAIN LOOP ===============
while running:
    user = input(f"{name}: ")

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

    elif user == "/exit":
        box("Goodbye!")
        break
    elif user == "/help":
    	print("")
    	print("_".center(60,"_"))
    	print("HELP".center(60))
    	print("")
    	time.sleep(0.2)
    	print("/inv")
    	time.sleep(0.2)
    	print("/fish")
    	time.sleep(0.2)
    	print("/rods")
    	time.sleep(0.2)
    	print("/selectrod")
    	print("/shop")
    	time.sleep(0.2)
    	print("/sell")
    	time.sleep(0.2)
    	print("/exit")
    	time.sleep(0.2)
    	print("/help")
    	time.sleep(0.2)
    	print("/bal")
    	print("")
    	print("_".center(60,"_"))
    	print("_")
    elif user == "/bal":
    	print("")
    	print("_".center(60,"_"))
    	print("")
    	print("Current Money :",money,"$")
    	print("")
    	print("_".center(60,"_"))
    	print("_")

    else:
        box("Unknown command!")