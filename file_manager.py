import csv
def load_csv(filename):
    inventory = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row["quantity"] = float(row["quantity"])
                    row["price"] = float(row["price"])
                    inventory.append(row)
                except ValueError:
                    print("Skipping invalid inventory row.")
            return inventory
    except FileNotFoundError:
        print("No previous Inventory file found.")
        print("Starting with an empty Inventory tracker.")
        return []



def save_csv(inventory, filename):
    if not inventory:
        print("No new inventory to save!")
        return 
    with open(filename, 'w', newline="") as file:
        writer = csv.DictWriter(file, fieldnames = inventory[0].keys())
        
        writer.writeheader()
        
        for product in inventory:
            writer.writerow(product)
    print("Inventory tracker saved successfully!")