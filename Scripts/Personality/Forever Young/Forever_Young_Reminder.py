# %%
def forever_young():
    """
    Forever Young Logic:
    - User inputs age
    - If age > 30 → mask it as 30
    - Path A: 30 - 9 = 21
    - Path B: 20 + 1 = 21
    """
    pivot = 30
    
    # Step 1: user input
    age = int(input("Enter your age: "))
    
    # Step 2: mask anything over 30 as 30
    if age > pivot:
        print(f"Age masked as {pivot} for calculation purposes.")
        age = pivot
    
    # Step 3: choose path
    choice = input("Choose your path (A or B): ").strip().lower()
    
    if choice == "a":
        path_a = pivot - 9
        print(f"Path A chosen → {path_a}. You are forever young!")
    elif choice == "b":
        path_b = 20 + 1
        print(f"Path B chosen → {path_b}. You are forever young!")
    else:
        print("Invalid choice! Please choose A or B.")
        return
    
    # Step 4: closing message
    print("Thank you for playing. Life is hard. Remember to keep your youth. ✨")
    
# Example run
forever_young()




