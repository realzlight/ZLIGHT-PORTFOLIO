#-------------------------------------------------------------------
# IMPORTING / VARIABLES
import time, random, os, threading

money = 100
inv = []
running = False
place = "shop"
lvl = 1
minlvl = 0
maxlvl = 15
shopstate = "Closed"
comprunning = False

# GLOBAL PRODUCT LIST
product = {
    "Hay's Chips": 5,
    "Dairy Milk": 10,
    "CocaCola": 20,
    "Fanta": 20,
    "Pepsi": 20,
    "Corn Flakes": 10,
    "Detergent": 10,
    "Soap": 10,
    "Hand Wash": 15,
    "Pencil": 5,
    "Eraser": 5,
    "Sharpner": 5,
    "Crayons": 5,
    "Rice": 20,
    "Ceral": 20,
    "Milk": 10,
    "Bread": 15,
    "Egg": 10
}

#-------------------------------------------------------------------
# UI FUNCTIONS
def d(): print("")
def b(): print("_"*60)
def w(int): time.sleep(int)
def p(str): print(str.center(60))

def shop():
    os.system("clear")
    d(); p("Shopify - Do /cmd"); d()
    p(shopname); d(); b(); d(); d()

#-------------------------------------------------------------------
# START GAME
def startgame():
    global name, shopname, running
    running = True
    d(); b(); d(); p("Shopify"); d()
    name = input("> What's Your Name >> "); d()
    shopname = input("> What Will Be Your Shop Name >> "); d(); d()
    shop()

#-------------------------------------------------------------------
# COMMANDS
def cmd():
    d(); b(); d(); p("COMMANDS"); d()
    print("/cmd - Toggle Cmd List"); d()
    print("/inv - Show Your Inventory"); d()
    print("/computer - Use Computer To Buy Items"); d()
    print("/leavecomputer - Leave Computer"); d()
    print("/openshop - Open Your Shop"); d()
    print("/closeshop - Close Your Shop"); d()
    print("/bal - Show Balance"); d()
    print("/lvl - Show Your Level"); d()
    print("/shopstate - Show Shop State"); d()
    b(); d()

#-------------------------------------------------------------------
# BALANCE
def bal():
    d(); b(); d(); p("Bank Balance"); d()
    print("Current Balance :","$",money); d()
    b(); d()

#-------------------------------------------------------------------
# LEVEL SYSTEM
def addpoint(points):
    global minlvl
    minlvl += points

def level():
    global lvl, minlvl, maxlvl
    if minlvl >= maxlvl:
        lvl += 1
        minlvl = 0
    d(); b(); d(); p("Level Stats"); d()
    print("Level :", lvl); d()
    print("Level Points :", minlvl); d()
    b(); d()

#-------------------------------------------------------------------
# CUSTOMER THREAD
customer_running = False

def customer_thread():
    global money, inv, customer_running, name, product,running

    while customer_running:
        time.sleep(random.randint(15, 30))

        if not customer_running:
            break

        # Random product from full product list
        order = random.choice(list(product.keys()))
        running = False
        d(); b(); d(); p("CUSTOMER"); d()
        print(f"Hey {name}! Do you have {order}? I want to buy one!")
        d()
        b()
        d()

        # Ask player
        customerinput = input("(yes/no) >>> ")
        d()

        if customerinput == "yes":
            if order in inv:
                inv.remove(order)
                money += product[order] + 5
                d(); p(f"Sold {order} for ${product[order] + 5}!"); d()
                addpoint(1)
                running = True
            else:
                d(); p("YOU DON'T HAVE THAT PRODUCT!"); d()
                running = True
        else:
            d()
            p("Customer left...")
            d()
            running = True
        

#-------------------------------------------------------------------
# COMPUTER SCREEN
def computer():
    os.system("clear")
    d(); p("Shopify"); d()
    p("COMPUTER - Do /cmd"); d()
    b(); d()

#-------------------------------------------------------------------
# STARTER MENU
d(); b(); d(); p("Shopify"); d()
p("1. PLAY"); d(); p("2. EXIT"); d()
b(); d()
playinput = input(" >> ")

if playinput == "1":
    startgame()
else:
    exit()

#-------------------------------------------------------------------
# MAIN LOOP
mode = "game"

while True:

    # ---------------- GAME MODE ----------------
    if mode == "game" and running:
        user = input(f"{name} > "); d()

        if user == "/cmd": cmd()
        elif user == "/bal": bal()
        elif user == "/lvl": level()

        elif user == "/shopstate":
            d(); b(); d(); p("SHOP STATE"); d()
            p(shopstate); d(); b(); d()

        elif user == "/openshop":
            shopstate = "Open"
            d(); p("Shop Opened!"); d()
            customer_running = True
            threading.Thread(target=customer_thread, daemon=True).start()

        elif user == "/closeshop":
            shopstate = "Closed"
            d(); p("Shop Closed!"); d()
            customer_running = False

        elif user == "/inv":
            if len(inv) == 0:
                d(); p("YOUR INVENTORY IS EMPTY!"); d()
            else:
                d(); b(); d(); p("INVENTORY"); d()
                for i in inv: print("•", i); d()
                b(); d()

        elif user == "/computer":
            if shopstate == "Open":
            	d()
            	p("Close Shop To Access Computer")
            	d()
            else:
                mode = "computer"
                running = False
                comprunning = True
                computer()

    # ---------------- COMPUTER MODE ----------------
    elif mode == "computer" and comprunning:
        compinput = input(" >> "); d()

        if compinput == "/cmd":
            d(); b(); d(); p("COMPUTER COMMANDS"); d()
            print("/shop"); d()
            print("/sales"); d()
            print("/leavecomputer"); d()
            b(); d()

        elif compinput == "/leavecomputer":
            comprunning = False
            running = True
            mode = "game"
            os.system("clear")
            d(); p("Shopify"); d(); p(shopname); d()
            b(); d()

        elif compinput == "/shop":
            d(); b(); d(); p("SHOP ITEMS"); d()

            for item in product:
                print(f"{item} - Buy ${product[item]}  Sell ${product[item] + 5}")
                d()

            b(); d()

            shopinput = input("> Enter Product Name >> ")

            if shopinput not in product:
                d(); p("INVALID PRODUCT NAME!"); d()
            else:
                cost = product[shopinput]
                if money >= cost:
                    inv.append(shopinput)
                    money -= cost
                    d(); p("PURCHASED SUCCESSFULLY!"); d()
                else:
                    d(); p("NOT ENOUGH MONEY!"); d()