def get_category():
    """Show the category menu, get the user's pick, and return the category name."""
    categories = {
        "1": "electronics",
        "2": "clothing",
        "3": "food & drinks",
        "4": "home & kitchen",
        "5": "office supplies",
    }
    while True:
        print("\nCategories:")
        print("1. Electronics")
        print("2. Clothing")
        print("3. Food & Drinks")
        print("4. Home & Kitchen")
        print("5. Office Supplies")
        choice = input("Please choose a number (1-5): ")
        if choice in categories:
            return categories[choice]
        print("Please enter a valid number!")




def get_number(prompt):
    """Ask for a non-negative number, re-prompting until valid. Returns a float."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Please enter a non-negative number!")
        except ValueError:
            print("Please enter a valid number!")