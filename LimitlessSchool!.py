# Importing
import time, os

# Important Variables
isadmin = False
running = True

# ================= BASIC DEFS =================
def b():
    print("_".center(60, "_"))
    print("")

def d():
    print("")

def t(ti):
    time.sleep(ti)

def p(s):
    print(s)

# ================= HELP =================
def help():
    d(); b(); d()
    p("HELP!".center(60)); d()
    cmds = ["/help", "/admin", "/addstd", "/removestd", "/searchstd", "/exit"]
    for c in cmds:
        t(0.15)
        p(c.center(60))
    d(); b(); d()

# ================= ADMIN SYSTEM =================
def admin():
    global isadmin

    if isadmin:
        d(); b()
        p("You Are Already Admin!".center(60))
        b(); d()
        return

    d(); b(); d()
    p("ADMIN PANEL".center(60)); d()

    adminint = input(" Enter Pass >> ")
    d(); b(); d()

    if adminint == "123":
        isadmin = True
        d(); b()
        p("Admin Access Granted!".center(60))
        b(); d()
    else:
        d(); b()
        p("Wrong Password!".center(60))
        b(); d()

# ================= STUDENT FUNCTIONS =================

# ---- Helper: Get class list ----
def get_class_list(c):
    return {
        "5": classv,
        "6": classvi,
        "7": classvii,
        "8": classviii,
        "9": classix,
        "10": classx
    }.get(c)

# ---- Add Student ----
def addstd():
    global isadmin
    if not isadmin:
        d(); b()
        p("ACCESS DENIED!".center(60))
        p("Admin Only Command".center(60))
        b(); d()
        return

    d(); b(); d()
    p("ADD STUDENT".center(60)); d()

    nameint = input(" Name >>> ")
    classint = input(" Class (5/6/7/8/9/10) >>> ")

    cl = get_class_list(classint)

    if cl is None:
        p("Invalid Class!".center(60))
        return

    cl.append(nameint)

    d(); b()
    p("Student Added!".center(60))
    b(); d()

# ---- Remove Student ----
def removestd():
    global isadmin
    if not isadmin:
        d(); b()
        p("ACCESS DENIED!".center(60))
        p("Admin Only Command".center(60))
        b(); d()
        return

    d(); b(); d()
    p("REMOVE STUDENT".center(60)); d()

    nameint = input(" Name >>> ")
    classint = input(" Class (5/6/7/8/9/10) >>> ")

    cl = get_class_list(classint)

    if cl is None:
        p("Invalid Class!".center(60))
        return

    if nameint in cl:
        cl.remove(nameint)
        d(); b()
        p("Student Removed!".center(60))
        b(); d()
    else:
        d(); b()
        p("Student Not Found!".center(60))
        b(); d()

# ---- Search Student ----
def searchstd():
    d(); b(); d()
    p("SEARCH STUDENT".center(60)); d()

    intclass = input(" Class (5/6/7/8/9/10) >>> ")

    cl = get_class_list(intclass)

    if cl is None:
        p("Invalid Class!".center(60))
        return

    d(); b(); d()
    p("Students:".center(60))
    d()

    if len(cl) == 0:
        p("No Students Found".center(60))
    else:
        for n in cl:
            print(n.center(60))
            t(0.15)

    d(); b(); d()

# ================= STARTER BANNER =================

d(); b(); d()
p("Limitless School!".center(60))
d()
p("Add/Remove Students And Search Students!".center(60))
d()
print("Type /help".center(60))
d(); d()

# ================= STUDENT LISTS =================
classv = []
classvi = []
classvii = []
classviii = []
classix = []
classx = []

# ================= MAIN LOOP =================
while running:
    print("")
    user = input(" >>>  ")
    print("")

    if user == "/help":
        help()
    elif user == "/admin":
        admin()
    elif user == "/addstd":
        addstd()
    elif user == "/removestd":
        removestd()
    elif user == "/searchstd":
        searchstd()
    elif user == "/exit":
        running = False
    elif user.strip() == "":
        d(); b()
        p("Invalid Command!".center(60))
        b(); d()
    else:
        d(); b()
        p("Unknown Command!".center(60))
        b(); d()