"""menus"""
name = input("Enter your name: ")
print("(H)ello\n(G)oodbye\n(Q)uit")
choice = input()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
        choice = input()
    elif choice == "G":
        print(f"Goodbye, {name}")
        choice = input()
    else:
        print("Invalid choice")
        choice = input()
print("Finished")
