MENU = """(H)ello
(G)oodbye
(Q)uit
"""
name = input("Enter name: ")
print(MENU, end="")
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU, end="")
    choice = input(">>> ").upper()
print("Finished.")