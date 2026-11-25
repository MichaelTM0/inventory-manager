from utils import get_number, get_category


def add_product(inventory):
    """Add a new product to the inventory, collecting its details from the user."""
    product = {}

    product["name"] = input("Please enter product name: ").strip().title()

    # Check if product already exists
    for existing_product in inventory:
        if existing_product["name"] == product["name"]:
            print(f"{product['name']} already exists in inventory.")
            return inventory

    product["quantity"] = get_number("Please enter the amount: ")
    product["price"] = get_number("Please enter the price: ")
    product["category"] = get_category()
    product["supplier"] = input("Please list the supplier for this item: ")
    product["last_updated"] = input("Please enter today's date (DD/MM/YY): ")

    inventory.append(product)
    print("Product saved successfully!")
    return inventory


def update_stock(inventory):
    """Update the price and/or quantity of an existing product."""
    found = False
    product_name = input("Which product would you like to update? ").strip().title()
    for product in inventory:
        if product["name"] == product_name:
            found = True
            while True:
                print("\nWhat would you like to update?")
                print("1. Price")
                print("2. Quantity")
                print("3. Both")

                option = input("Please enter a choice (1-3): ")

                if option not in ["1", "2", "3"]:
                    print("Please enter a valid choice.")
                    continue

                if option in ["1", "3"]:
                    product["price"] = get_number("Please enter the new price: ")

                if option in ["2", "3"]:
                    product["quantity"] = get_number("Please enter the new quantity: ")

                product["last_updated"] = input("Please enter today's date (DD/MM/YY): ")
                break
    if not found:
        print("Product not found.")
    return inventory


def display_product(product):
    """Print a single product's details in a formatted block."""
    print("\n" + "=" * 40)
    print(f"Product: {product['name']}")
    print(f"Category: {product['category'].title()}")
    print(f"Quantity: {product['quantity']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Supplier: {product['supplier']}")
    print(f"Last Updated: {product['last_updated']}")
    print("=" * 40)


def category_search(inventory):
    """Search the inventory for products in a chosen category and display them."""
    category = get_category()

    found = False
    for product in inventory:
        if product["category"] == category:
            display_product(product)
            found = True

    if not found:
        print("No products exist in this category.")


LOW_STOCK_LIMIT = 5


def check_low_stock(inventory):
    """Print every product at or below the low-stock limit."""
    for product in inventory:
        if product["quantity"] <= LOW_STOCK_LIMIT:
            print(f"{product['name']} only has {product['quantity']} left!")