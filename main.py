from file_manager import load_csv, save_csv
from inventory import add_product, update_stock, category_search, check_low_stock


def main(inventory):
    print("\n" + "=" * 50)
    print("             INVENTORY TRACKER")
    print("=" * 50)
   
    
    while True:
        print("\n" + "="*50)
        print("1. Add Product")
        print("2. Update Stock")
        print("3. Search by category")
        print("4. Check Low Stock")
        print("5. Save and exit")
        print("6. Exit without saving")
        print("="*50)
        
        option = input("Please select a number (1-6): ")
        
        if option == "1":
            inventory = add_product(inventory)
        elif option == "2":
            inventory = update_stock(inventory)
        elif option == "3":
            category_search(inventory)
        elif option == "4":
            check_low_stock(inventory)
        elif option == "5":
            save_csv(inventory, "inventory.csv")
            print("Goodbye!")
            break
        elif option == "6":
            print("Thanks for using the inventory tracker!")
            break
        else:
            print("Please enter a valid number.")
            


if __name__ == "__main__":
    inventory = load_csv("inventory.csv")
    main(inventory)
        