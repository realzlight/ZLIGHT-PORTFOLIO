# IMPORTING
import os, time, random, threading

isadmin = False
library = {}
index = []

# FUNCTIONS
def b():
    print("_".center(60, "_"))

def help():
    print("")
    b()
    print("")
    print("Help".center(60))
    print("")
    print("1. /admin")
    print("2. /help")
    print("3. /addbook")
    print("4. /removebook")
    print("5. /search")
    print("6. /index")
    print("")
    b()
    print("")

def admin():
    global isadmin

    if isadmin:
        print("\nYou are Already An Admin\n")
        return
    
    print("")
    b()
    print("")
    print("ADMIN PANEL".center(60))
    print("")
    adminchoice = input("Enter Admin Pass >> ")

    if adminchoice == "123":
        print("\nAccess Granted!")
        b()
        print("")
        isadmin = True
    else:
        print("\nWrong Password!\n")

def addbook():
    if not isadmin:
        print("\nCan't Add Book, Admin Required!\n")
        return

    print("")
    b()
    print("")
    print("ADD BOOK".center(60))
    print("")

    book = input("Enter Book Name >> ")
    print("")
    bookcon = input("Enter Book Content >> ")
    print("")

    library[book] = bookcon
    index.append(book)

    print("Successfully Added Book!")
    b()
    print("")
    print(f"Saved '{book}' in library!\n")

def search_book():
    bookname = input("Enter Book Name >> ")
    print("")

    if bookname in library:
        print("")
        b()
        print("")
        print(bookname.center(60))
        print("")
        print(library[bookname])
        print("")
        b()
        print("")
    else:
        print("")
        b()
        print("")
        print("Book Not Found!".center(60))
        print("")
        b()
        print("")

def show_index():
    print("")
    b()
    print("")
    print("BOOK INDEX".center(60))
    print("")
    if len(index) == 0:
        print("No Books Added Yet!".center(60))
    else:
        for i, book in enumerate(index, 1):
            print(f"{i}. {book}".center(60))
    print("")
    b()
    print("")


# STARTER BANNER
print("")
b()
print("")
print("Limitless Library!".center(60))
print("")
print("You Can Add/Remove And Search".center(60))
print("")
name = input("Enter Name >> ")
print("\n")


# MAIN LOOP
running = True
while running:
    user = input(f"{name} >> ")

    if user == "/help":
        help()

    elif user == "/admin":
        admin()

    elif user == "/addbook":
        addbook()

    elif user == "/search":
        search_book()

    elif user == "/index":
        show_index()

    elif user == "/exit":
        running = False

    print("")