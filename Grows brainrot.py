import time
import threading
import random
import os
#Statter Banner
running = False
print("")
time.sleep(0.5)
print("_".center(60,"_"))
print("")
time.sleep(0.2)
print("Grow A Brainrot".center(60))
print("")
time.sleep(0.2)
print("1. Play".center(60))
print("")
time.sleep(0.2)
print("2. Quit".center(60))
print("")
time.sleep(0.5)
print("_".center(60,"_"))
print("")
time.sleep(0.2)
name = input("Enter Your Name : ")
print("")
menuinput = int(input(" >>>  "))

if menuinput == 1:
	time.sleep(0.5)
	os.system("clear")
	time.sleep(0.2)
	running = True
	print("")
	time.sleep(0.5)
	print("_".center(60,"_"))
	print("")
	time.sleep(0.2)
	print("Grow A Brainrot".center(60))
	print("")
	
else :
	time.sleep(0.5)
	running = False
	













# ----------------- CONFIG -----------------
INVENTORY_SIZE = 5
SHOP_REFRESH = 300  # 5 minutes in seconds
MONEY_PER_TICK = 1  # Base generates money every 1 min
TICK_INTERVAL = 60   # 60 seconds per money tick

# Brainrot definitions
brainrots = {
    "Common Brainrot": {"rank": 1, "chance": 0.5, "income": 1},
    "Uncommon Brainrot": {"rank": 2, "chance": 0.3, "income": 2},
    "Rare Brainrot": {"rank": 3, "chance": 0.15, "income": 5},
    "Legendary Brainrot": {"rank": 4, "chance": 0.05, "income": 10},
}

# ----------------- GAME STATE -----------------
inventory = []
base = []
money = 1000
shop = []

# ----------------- SHOP FUNCTIONS -----------------
def generate_shop():
    global shop
    shop = []
    while len(shop) < 5:
        for name, data in brainrots.items():
            if random.random() <= data["chance"]:
                shop.append(name)
            if len(shop) >= 5:
                break

def shop_tick():
    while True:
        generate_shop()
        time.sleep(SHOP_REFRESH)  # refresh every 5 min

# ----------------- MONEY TICK -----------------
def base_income_tick():
    global money
    while True:
        total_income = sum(brainrots[b]["income"] for b in base)
        money += total_income
        if total_income > 0:
            print(f"💰 Your base generated {total_income} braincoin! Total: {money}")
        time.sleep(TICK_INTERVAL)

# ----------------- INVENTORY FUNCTIONS -----------------
def add_to_inventory(item):
    if len(inventory) < INVENTORY_SIZE:
        inventory.append(item)
        print(f"✅ Added '{item}' to your inventory!")
    else:
        print("❌ Inventory full!")

def move_to_base(item_index):
    if 0 <= item_index < len(inventory):
        item = inventory.pop(item_index)
        base.append(item)
        print(f"🏠 Moved '{item}' to your base.")
    else:
        print("❌ Invalid inventory slot!")

def show_inventory():
    print("")
    print("_".center(60,"_"))
    print("_")
    print("Inventory".center(60))
    for i, item in enumerate(inventory, 1):
        print(f"{i}. {item}")
        print("")
    
    print("")
    if not inventory:
        print("Inventory is empty!")
        print("_".center(60,"_"))

def show_base():
    print("\n🏠 Base:")
    for i, item in enumerate(base, 1):
        print(f"{i}. {item} (Income: {brainrots[item]['income']}/min)")
    if not base:
        print("Base is empty!")

def show_shop():
    print("\n🛒 Shop:")
    for i, item in enumerate(shop, 1):
        print(f"{i}. {item} (Income: {brainrots[item]['income']}/min)")

# ----------------- MAIN LOOP -----------------
def game_loop():
    global money
   
    while running:
        command = input(f"\n{name} :" ).strip()
        
        if command == "/shop":
            show_shop()
        elif command.startswith("/buy "):
            try:
                index = int(command[5:]) - 1
                if 0 <= index < len(shop):
                    add_to_inventory(shop.pop(index))
                else:
                    print("❌ Invalid shop slot!")
            except:
                print("❌ Invalid input!")
        elif command == "/inv":
            show_inventory()
        elif command == "/base":
            show_base()
        elif command.startswith("/move "):
            try:
                index = int(command[6:]) - 1
                move_to_base(index)
            except:
                print("❌ Invalid input!")
        elif command == "/money":
            print(f"💰 Money: {money}")
        elif command == "/exit":
            print("Exiting game...")
            break
        else:
            print("❌ Unknown command!")

# ----------------- START THREADS -----------------
threading.Thread(target=shop_tick, daemon=True).start()
threading.Thread(target=base_income_tick, daemon=True).start()

# ----------------- RUN GAME -----------------
game_loop()