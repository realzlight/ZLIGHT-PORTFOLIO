# IMPORTING
import time, random, os, threading
items = ["Furnance","Trap"]

for item in items:
    print("• " + item)

tool = [
    {"name": "Wooden Axe", "dura": 20},
    {"name": "Wooden Pickaxe", "dura": 20},
    {"name": "Wooden Sword", "dura": 20},
    {"name": "Fishing Rod", "dura": 25}
]
#running = False
Current = "Day"
cycle = True
place = "Plains"

# ===================== PLAYER STATS =====================

health_max = 10
health_points = 10

hunger_max = 10
hunger_points = 10

running = True

# ===================== SAFE THREAD LOCK =====================

stat_lock = threading.Lock()

# UI HELPERS
#def d(): print("")
#def b(): print("_" * 60)
#def p(msg): print(msg)
#def w(t): time.sleep(t)

# ===================== DISPLAY BARS =====================

def get_hunger_bar():
    d(); b(); d()
    p("HUNGER")
    d()
    print("  HUNGER >", "🍗" * hunger_points if hunger_points > 0 else "❌")
    d(); b(); d()

def get_health_bar():
    d(); b(); d()
    p("HEALTH")
    d()
    print("  HEALTH >", "❤️" * health_points if health_points > 0 else "💀")
    d(); b(); d()

# ===================== HUNGER SYSTEM =====================

def hunger_loop():
    global hunger_points, health_points, running

    while running:
        time.sleep(30)  # Hunger drains slower

        with stat_lock:
            hunger_points -= 1

            # ⚠️ HUNGER WARNING
            if hunger_points == 1:
                print("\n" + "_"*60)
                print("⚠️ Warning: Last hunger point!")
                print("_"*60)

            # ❌ NO HUNGER → Lose Health!
            if hunger_points <= 0:
                hunger_points = 0
                health_points -= 1
                print("\n💀 You are starving! Losing health!")

                if health_points <= 0:
                    running = False
                    print("\nYOU STARVED TO DEATH!")
                    break


# ===================== HEALTH SYSTEM =====================

def health_loop():
    global health_points, hunger_points, running

    regen_timer = 0

    while running:

        time.sleep(1)

        with stat_lock:
            # ⚠️ LOW HEALTH
            if health_points == 1:
                print("\n" + "_"*60)
                print("⚠️ Warning: Last Health point!")
                print("_"*60)

            # ❌ DEAD
            if health_points <= 0:
                health_points = 0
                print("\nYOU DIED!")
                running = False
                break

            # ❤️ AUTO HEALTH REGEN (only if hunger > 3)
            if hunger_points > 3 and health_points < health_max:
                regen_timer += 1
                if regen_timer >= 5:  # heal every 5 sec
                    health_points += 1
                    regen_timer = 0
                    print("❤️ Auto-Regen +1 Health")

            else:
                regen_timer = 0  # Regen stops when hunger low


# ===================== START THREADS =====================

def start_status_threads():
    threading.Thread(target=hunger_loop, daemon=True).start()
    threading.Thread(target=health_loop, daemon=True).start()
#-------------------------------------------------------------------
# DEF
def d():
    print("")

def b():
    print("_" * 60)

def p(str):
    print(str.center(60))

def w(int):
    time.sleep(int)
    
# DAYLIGHT CYCLE
def daynight():
    global Current, cycle
    while cycle:
        Current = "Day"
        d(); b(); d()
        p("CURRENTLY IS DAY. THE NIGHT WILL ARISE AFTER 2 MIN")
        d(); b(); d()
        time.sleep(120)

        Current = "Night"
        d(); b(); d()
        p("CURRENTLY IS NIGHT! DAY WILL ARISE AFTER 2 MIN")
        d(); b(); d()
        time.sleep(120)

def reduce_durability(tool_name, amount):
    for t in tool:
        if t["name"] == tool_name:
            t["dura"] -= amount
            
            if t["dura"] <= 0:
                p(f"{tool_name} Broke!")
                tool.remove(t)
            else:
                p(f"{tool_name} Durability: {t['dura']}")
            return

# ===================== MINING SYSTEM =====================

# Drop chances (you can adjust)
mineral_chances = {
    "Stone": 60,
    "Iron": 20,
    "Gold": 10,
    "Diamond": 5
}

def get_random_mineral():
    roll = random.randint(1, 100)
    chance_sum = 0
    
    for mineral, chance in mineral_chances.items():
        chance_sum += chance
        if roll <= chance_sum:
            return mineral
    return "Stone"


def mine_animation(seconds):
    d()
    p("Mining...")
    for i in range(seconds):
        time.sleep(1)
        print("⛏️...", i + 1)
    d()


# >>> WOODEN PICKAXE MINING
def mine_with_wood_pickaxe():
    d(); b(); d()
    p("MINING WITH WOODEN PICKAXE")
    d()

    for i in range(10):
        mineinput = input("> Enter M To Mine > ")
        if mineinput.upper() != "M":
            p("Stopped Mining")
            return

    mine_animation(4)

    mined = get_random_mineral()
    items.append(mined)
    p(f"Successfully mined 1x {mined}!")
    reduce_durability("Wooden Pickaxe", 1)
    d(); b(); d()


# >>> IRON PICKAXE MINING
def mine_with_iron_pickaxe():
    d(); b(); d()
    p("MINING WITH IRON PICKAXE")
    d()

    for i in range(7):
        mineinput = input("> Enter M To Mine > ")
        if mineinput.upper() != "M":
            p("Stopped Mining")
            return

    mine_animation(3)

    mined = get_random_mineral()
    items.append(mined)
    p(f"Successfully mined 1x {mined}!")
    reduce_durability("Iron Pickaxe", 1)
    d(); b(); d()


# >>> GOLDEN PICKAXE MINING
def mine_with_gold_pickaxe():
    d(); b(); d()
    p("MINING WITH GOLD PICKAXE")
    d()

    for i in range(8):
        mineinput = input("> Enter M To Mine > ")
        if mineinput.upper() != "M":
            p("Stopped Mining")
            return

    mine_animation(2)

    mined = get_random_mineral()
    items.append(mined)
    p(f"Successfully mined 1x {mined}!")
    reduce_durability("Golden Pickaxe", 1)
    d(); b(); d()


# >>> DIAMOND PICKAXE MINING
def mine_with_diamond_pickaxe():
    d(); b(); d()
    p("MINING WITH DIAMOND PICKAXE")
    d()

    for i in range(3):
        mineinput = input("> Enter M To Mine > ")
        if mineinput.upper() != "M":
            p("Stopped Mining")
            return

    mine_animation(1)

    mined = get_random_mineral()
    items.append(mined)
    p(f"Successfully mined 1x {mined}!")
    reduce_durability("Diamond Pickaxe", 1)
    d(); b(); d()
	
	
def cutwithwoodaxe():
	d()
	b()
	d()
	p("CUTTING WITH WOODEN AXE")
	d()
	for i in range(10):
		cutinput = input("> Enter C To Cut > ")
	d()
	p("Cutting The Tree....")
	w(5)
	d()
	items.append("Wood")
	p("Successfully Cut The Tree!, 1x Wood Added")
	reduce_durability("Wooden Axe",1)
	d()
	b()
	d()

def cutwithironaxe():
	d()
	b()
	d()
	p("CUTTING WITH IRON AXE")
	d()
	for i in range(7):
		cutinput = input("> Enter C To Cut > ")
	d()
	p("Cutting The Tree....")
	w(3)
	d()
	items.append("Wood")
	p("Successfully Cut The Tree!, 1x Wood Added")
	reduce_durability("Iron Axe",1)
	d()
	b()
	d()

def cutwithgoldaxe():
	d()
	b()
	d()
	p("CUTTING WITH GOLD AXE")
	d()
	for i in range(9):
		cutinput = input("> Enter C To Cut > ")
	d()
	p("Cutting The Tree....")
	w(4)
	d()
	items.append("Wood")
	p("Successfully Cut The Tree!, 1x Wood Added")
	reduce_durability("Golden Axe",1)
	d()
	b()
	d()

def cutwithdiamondaxe():
	d()
	b()
	d()
	p("CUTTING WITH DIAMOND AXE")
	d()
	for i in range(10):
		cutinput = input("> Enter C To Cut > ")
	d()
	p("Cutting The Tree....")
	w(5)
	d()
	items.append("Wood")
	p("Successfully Cut The Tree!, 1x Wood Added")
	reduce_durability("Diamond Axe",1)
	d()
	b()
	d()

def cutwithstoneaxe():
	d()
	b()
	d()
	p("CUTTING WITH STONE AXE")
	d()
	for i in range(8):
		cutinput = input("> Enter C To Cut > ")
	d()
	p("Cutting The Tree....")
	w(4)
	d()
	items.append("Wood")
	p("Successfully Cut The Tree!, 1x Wood Added")
	reduce_durability("Stone Axe",1)
	d()
	b()
	d()

# ===================== FISHING SYSTEM =====================

fish_loot = [
    "Astral Damshell Fish",
    "Astral Salmon Fish",
    "Blop Fish",
    "Contelope Puffer",
    "Monk Fish"
]
def get_random_fish():
    return random.choice(fish_loot)

def fishing_animation():
    d()
    p("FISHING...")
    for i in range(3):
        time.sleep(1)
        print("🎣...", i+1)
    d()


def fish():
    d(); b(); d()
    p("FISHING")
    d()
    fishtimer = random.randint(3,5)
    w(fishtimer)

    for i in range(5):
        pull = input("> Enter P to Pull > ")
        if pull.upper() != "P":
            p("Stopped Fishing")
            return

    fishing_animation()
    caught = get_random_fish()
    items.append(caught)
    p(f"🎣 You caught: {caught}!")
    reduce_durability("Fishing Rod", 1)
    d(); b(); d()		
		

def startgame():
    d()
    b()
    d()
    global name
    name = input(" Enter Your Name >>   ")
    d()
    b()
    d()

    os.system("clear")
    d()
    b()
    d()
    time.sleep(0.5)
    p("ForgeRealm")
    d()
    p("Plains")
    d()
    d()

    global running
    running = True

    # 🌞 Start day/night cycle (thread)
    threading.Thread(target=daynight, daemon=True).start()

    # 🍗❤️ Start hunger + health threads
    start_status_threads()

# FIX: WOODS FUNCTION
def woods():
    global place
    place = "Woods"
    os.system("clear")
    d()
    b()
    d()
    p("ForgeRealm")
    d()
    p("Woods")
    d()
    d()
    d()


# COMMAND LIST
def cmd():
    d()
    w(0.2)
    b()
    d()
    w(0.2)
    p("COMMANDS")
    d()
    w(0.2)
    print("/cmd - Toggle A List Of Cmds")
    d()
    w(0.2)
    print("/cave - Take You To Caves Where You Can Mine Minerals And Stone")
    d()
    w(0.2)
    print("/lake - Take You To Lake Where You Can Fish")
    d()
    w(0.2)
    print("/woods - Take You To Woods Where You Can Mine Woods")
    d()
    w(0.2)
    print("/craft - Toggle A List Of Crafting Recipes")
    d()
    w(0.2)
    print("/furnance - To Cook Food To Eat")
    d()
    w(0.2)
    print("/inv - Show Inventory")
    d()
    w(0.2)
    print("/tools - Show Tools")
    d()
    w(0.2)
    print("/cut - Cut Wood If You In Woods")
    d()
    w(0.2)
    print("/mine - Mine Anything If In Cave")
    d()
    w(0.2)
    print("/hunger - Check Hunger Points")
    d()
    w(0.2)
    print("/health - Check Health Points")
    d()
    w(0.2)
    print("/tool - To Toggle Tool Inventory")
    d()
    w(0.2)
    print("/plain - To Go To Plains")
    d()
    w(0.2)
    print("/trap - To Set Trap For Chicken")
    d()
    w(0.2)
    print("/eat - To eat Cooked Food")
    d()
    w(0.2)
    print("/fish - To Catch Fish In Lake")
    d()
    w(0.2)
    print("/fact - For Info About This Game")
    d()
   
    
    

    
    b()
    d()
def furnance():
    d()
    b()
    d()
    p("FURNACE")
    d()

    furnanceinput = input("> Enter Food Name To Cook > ")

    # ------------------------------------------------------
    # A dictionary for cooking (Cleaner & scalable)
    # ------------------------------------------------------
    cookables = {
        "Astral Damshell Fish": "Cooked Astral Damshell Fish",
        
        "Astral Salmon Fish": "Cooked Astral Salmon Fish",
        
        "Monk Fish": "Cooked Monk Fish",
        
        "Blop Fish": "Cooked Blop Fish",
        
        "Contelope Puffer": "Cooked Contelope Puffer",
        
        "Chicken":"Cooked Chicken"
    }

    # Check if input is valid
    if furnanceinput not in cookables:
        p("❌ Invalid Food Name!")
        return

    # Check if user has that food
    if furnanceinput not in items:
        p(f"❌ You don't have a {furnanceinput}!")
        return

    # Remove raw food
    items.remove(furnanceinput)

    # Cooking animation
    p("Cooking...")
    d()
    for i in range(5):
        print("Cooking....")
        time.sleep(0.5)

    d()
    p("✔ Cooked Successfully!")
    d()
    b()
    d()

    # Add cooked item
    items.append(cookables[furnanceinput])
    
    
    
trap_set = False
trap_ready = False
trapdura = 10

def trap():
    global trap_set, trap_ready, trapdura

    d()
    b()
    d()
    p("TRAP")
    d()

    if trap_set:
        p("⚠ A trap is already set! You need to wait or reset it.")
        d(); b(); d()
        return

    # Setting trap animation
    for i in range(5):
        print("Setting Trap.....")
        time.sleep(0.5)

    d()
    b()
    d()
    p("✔ Trap has been successfully set!")
    d()
    b()
    d()

    trap_set = True
    trap_ready = True
    
    # Random time until something is trapped
    traptime = random.randint(15, 30)

    def trap_timer():
        global trap_set, trap_ready, trapdura
        time.sleep(traptime)
        d()
        b()
        d()
        if trapdura > 0:
            p(f"TRAPPED SOMETHING!")
            p(f"You Caught A Chicken! Trap Durability: {trapdura}")
            items.append("Chicken")
            trapdura -= 1

            if trapdura == 0:
                if "Trap" in items:
                    items.remove("Trap")
                p("❌ Your trap broke!")
        else:
            p("❌ Trap is broken! You need a new one.")

        d()
        b()
        d()
        # Trap stops after catching
        trap_set = False
        trap_ready = False

    threading.Thread(target=trap_timer, daemon=True).start()
  
def eat():
    global hunger_points  # Important, so we can modify hunger
    eatable = ["Cooked Astral Damshell Fish", "Cooked Astral Salmon Fish", "Cooked Chicken", "Cooked Contelope Puffer", "Cooked Monk Fish"]
    
    d()
    b()
    d()
    p("EAT")
    d()

    eatinput = input("> ENTER FOOD NAME TO EAT > ")

    # Check if food is in inventory and eatable
    if eatinput in eatable:
        if eatinput not in items:
            p(f"❌ You don't have {eatinput} in your inventory!")
            return

        if hunger_points >= hunger_max:
            d()
            b()
            d()
            p("YOU HAVE FULL HUNGER BAR")
            d()
            b()
            d()
        else:
            items.remove(eatinput)
            hunger_points += 1
            if hunger_points > hunger_max:  # prevent going over max
                hunger_points = hunger_max

            d()
            b()
            d()
            p("YOU HAVE EATEN FOOD SUCCESSFULLY! HUNGER INCREASED")
            d()
            b()
            d()
    else:
        p("❌ You can't eat that!")

def craft():
    d()
    b()
    d()
    p("🛠️  CRAFTING MENU  🛠️")
    d()
    
    # List of craftable items
    craftables = [
        "1. Furnace",
        "2. Wooden Axe",
        "3. Stone Axe",
        "4. Iron Axe",
        "5. Golden Axe",
        "6. Diamond Axe",
        "7. Wooden Pickaxe",
        "8. Stone Pickaxe",
        "9. Iron Pickaxe",
        "10. Golden Pickaxe",
        "11. Diamond Pickaxe",
        "12. Trap",
        "13. Fishing Rod",
        "14. Stick"
    ]
    
    # Display crafting items in a neat format
    for item in craftables:
        p(item)
    
    d()
    choice = input("> Enter Crafting Number To Craft > ").strip()

    # Dictionary of recipes
    recipes = {
        "1": {"name": "Furnace", "materials": {"Stone": 8}},
        "2": {"name": "Wooden Axe", "materials": {"Wood": 3, "Stick": 2}},
        "3": {"name": "Stone Axe", "materials": {"Stone": 3, "Stick": 2}},
        "4": {"name": "Iron Axe", "materials": {"Iron": 3, "Stick": 2}},
        "5": {"name": "Golden Axe", "materials": {"Gold": 3, "Stick": 2}},
        "6": {"name": "Diamond Axe", "materials": {"Diamond": 3, "Stick": 2}},
        "7": {"name": "Wooden Pickaxe", "materials": {"Wood": 3, "Stick": 2}},
        "8": {"name": "Stone Pickaxe", "materials": {"Stone": 3, "Stick": 2}},
        "9": {"name": "Iron Pickaxe", "materials": {"Iron": 3, "Stick": 2}},
        "10": {"name": "Golden Pickaxe", "materials": {"Gold": 3, "Stick": 2}},
        "11": {"name": "Diamond Pickaxe", "materials": {"Diamond": 3, "Stick": 2}},
        "12": {"name": "Trap", "materials": {"Iron": 5}},
        "13": {"name": "Fishing Rod", "materials": {"Stick": 3, "String": 2}},
        "14": {"name": "Stick", "materials": {"Wood": 1}}
    }

    if choice not in recipes:
        p("❌ Invalid Choice!")
        return

    item_name = recipes[choice]["name"]
    materials = recipes[choice]["materials"]

    # Check for materials in inventory
    missing = []
    for mat, amt in materials.items():
        if items.count(mat) < amt:
            missing.append(f"{amt}x {mat}")

    if missing:
        d()
        p("❌ You are missing:")
        for m in missing:
            p(f"   • {m}")
        return

    # Show recipe nicely
    d()
    b()
    d()
    p(f"Crafting: {item_name}")
    p("Required Materials:")
    for mat, amt in materials.items():
        p(f"   • {amt}x {mat}")
    d()
    confirm = input("> Craft this item? (yes/no) > ").strip().lower()
    if confirm != "yes":
        p("❌ Crafting cancelled!")
        return

    # Remove materials
    for mat, amt in materials.items():
        for _ in range(amt):
            items.remove(mat)

    # Add crafted item
    if item_name == "Stick":
        for _ in range(4):
            items.append("Stick")
        p("✔ Successfully crafted 4 Sticks!")
    else:
        items.append(item_name)
        p(f"✔ Successfully crafted {item_name}!")

    d()
    b()
    d()
#-------------------------------------------------------------------
# STARTER BANNER
d()
b()
d()
p("ForgeRealm")
d()
p("1. PLAY")
d()
p("2. QUIT")
d()
b()
d()

maininput = input(" >>>  ")

if maininput == "1":
    os.system("clear")
    startgame()

elif maininput == "2":
    print("")
    p("Game Quit")


#-------------------------------------------------------------------
# MAIN LOOP
while running:
    user = input(f"{name} >>  ")
    d()

    if user.startswith("/cmd"):
        cmd()

    elif user.startswith("/woods"):
        woods()

    elif user.startswith("/cut"):
        if place != "Woods":
            d()
            p("Not In Woods")
        else:
            axeinput = input("> Enter Axe Name > ")  # Added missing input
            selected_tool = None
            for t in tool:
                if t["name"] == axeinput:
                    selected_tool = t
                    break

            if selected_tool is None:
                p("Invalid Tool Or Not In Inventory")
            else:
                if axeinput == "Wooden Axe":
                    cutwithwoodaxe()
                elif axeinput == "Iron Axe":
                    cutwithironaxe()
                elif axeinput == "Golden Axe":
                    cutwithgoldaxe()
                elif axeinput == "Diamond Axe":
                    cutwithdiamondaxe()
                elif axeinput == "Stone Axe":
                	cutwithstoneaxe()

    elif user.startswith("/inv"):
        d()
        b()
        d()
        p("INVENTORY")
        d()
        if len(items) == 0:
            print("• (Empty)")
        else:
            for item in items:
                print("• " + item)
        d()
        b()
        d()

    elif user.startswith("/tool"):
        d()
        b()
        d()
        p("TOOLS")
        d()
        if len(tool) == 0:
            print("• (Empty)")
        else:
            for t in tool:
                print(f"• {t['name']} — Durability: {t['dura']}")
        d()
        b()
        d()
    elif user.startswith("/plain"):
    	os.system("clear")
    	d()
    	b()
    	d()
    	p("ForgeRealm")
    	d()
    	p("Plain")
    	d()
    	d()
    elif user.startswith("/hunger"):
    	get_hunger_bar()
    elif user.startswith("/health"):
        get_health_bar()
    elif user.startswith("/cave"):
    	os.system("clear")
    	place = "Cave"
    	d()
    	b()
    	d()
    	p("ForgeRealm")
    	d()
    	p("Cave")
    	d()
    	d()
    	
    elif user.startswith("/mine"):
        if place != "Cave":
            d()
            p("Not In Cave")
        else:
            pickinput = input("> Enter Pickaxe Name > ")
            selected_tool = None

        # Check if player actually owns the pickaxe
            for t in tool:
                if t["name"] == pickinput:
                    selected_tool = t
                    break

            if selected_tool is None:
                p("You do NOT have this pickaxe in your inventory!")
            else:
                if pickinput == "Wooden Pickaxe":
                    mine_with_wood_pickaxe()
                elif pickinput == "Iron Pickaxe":
                    mine_with_iron_pickaxe()
                elif pickinput == "Golden Pickaxe":
                    mine_with_gold_pickaxe()
                elif pickinput == "Diamond Pickaxe":
                    mine_with_diamond_pickaxe()
                elif pickinput == "Stone Pickaxe":
                   mine_with_stone_pickaxe()
    elif user.startswith("/fish"):
        if place != "Lake":
            p("Not In Lake")
        else:
        # Check if player has the fishing rod
            if not any(t["name"] == "Fishing Rod" for t in tool):
                p("❌ You don't have a Fishing Rod!")
            else:
            	fish()
    elif user.startswith("/lake"):
    	os.system("clear")
    	d()
    	b()
    	d()
    	p("ForgeRealm")
    	d()
    	p("Lake")
    	d()
    	place = "Lake"
    elif user.startswith("/furnance"):
    	if "Furnance" not in items:
    		p(" You don't have a Furnance!")
    	else:
    		furnance()
    elif user.startswith("/trap"):
    	if "Trap" not in items:
    		p("You don't have a Trap!")
    	else:
    		trap();
    elif user.startswith("/eat"):
    	eat()
    elif user.startswith("/craft"):
    	craft()
    elif user.startswith("/fact"):
    	d()
    	d()
    	b()
    	p("FACTS!")
    	d()
    	print("HERE YOU CAN SURVIVE BY EATING FOOD. YOU CAN SET TRAP, DO FISHING AND COOK FOOD TO EAT MAKE TOOLS BY CRAFTING CUT TREES AND GET STONE AND MINERALS BY MINIGING DO /lake TO GO TO LAKE WHERE YOU CAN /fish TO CATCH FISHES DO /cave WHERE YOU CAN /mine TO GET MINERAL AND STONES DO /woods WHERE YOU CAN /cut TO CUT TREES FOR WOODS AND DO /craft TO CRAFT THINGS")
    	d()
    	b()
   
   

   