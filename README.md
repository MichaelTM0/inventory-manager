# Inventory Tracker (Multi-File)

A command-line inventory management system built in Python, organized as a **multi-file program** to practice modules, imports, and separation of concerns. It tracks products, their stock levels, prices, categories, and suppliers, and saves everything to a CSV file so the data persists between runs.

This project is a **refactor** of an earlier single-file version — the same functionality, reorganized into four focused files that each handle one responsibility.

## Features

* **Add products** with name, quantity, price, category, supplier, and last-updated date
* **Duplicate protection** — warns if a product already exists instead of adding it twice
* **Update stock** — change a product's price, quantity, or both
* **Search by category** — view all products in a chosen category
* **Low-stock alerts** — flag any product at or below the low-stock limit
* **Input validation** — non-numeric or negative entries are caught and re-prompted
* **CSV persistence** — load existing inventory on start, save changes on exit
* **Save-and-exit or exit-without-saving** options

## Requirements

* Python 3.6 or newer
* No external packages — uses only Python's built-in `csv` module

## Getting Started

1. Clone the repository (update the URL if your repo name differs):

   ```bash
   git clone https://github.com/MichaelTM0/inventory-tracker.git
   cd inventory-tracker
   ```

2. Run the program (all four `.py` files must be in the same folder):

   ```bash
   python main.py
   ```

   On the first run it starts with an empty inventory; your data is saved to `inventory.csv`.

## Usage

```
==================================================
             INVENTORY TRACKER
==================================================
1. Add Product
2. Update Stock
3. Search by Category
4. Check Low Stock
5. Save and Exit
6. Exit Without Saving
==================================================
Please select a number (1-6):
```

## How It Works

The program is split across four files, each with a single responsibility:

* **`main.py`** — the driver. Runs the menu loop, routes each choice to the right function, loads the inventory once at startup, and saves on exit. Imports what it needs from the other three files.
* **`inventory.py`** — the inventory logic. The operations that work on the in-memory inventory: `add_product`, `update_stock`, `category_search`, `check_low_stock`, and `display_product`.
* **`file_manager.py`** — the persistence layer. Reads and writes the CSV file: `load_csv` and `save_csv`.
* **`utils.py`** — reusable helpers. Input-validation functions used across the program: `get_number` (validated numeric input) and `get_category` (menu-driven category selection).

`main.py` ties the pieces together with imports:

```python
from file_manager import load_csv, save_csv
from inventory import add_product, update_stock, category_search, check_low_stock
from utils import get_number, get_category
```

This demonstrates **separation of concerns** — the file I/O, the inventory logic, the input helpers, and the program flow each live in their own module. Changing how data is stored only touches `file_manager.py`; the inventory logic stays untouched. Repeated input-validation code was pulled into `utils.py` once (DRY) and reused everywhere instead of being copy-pasted into each function.

The program also uses the `if __name__ == "__main__":` guard so `main.py` runs the menu when launched directly, while the other modules can be imported without side effects.

## What I Learned

* Refactoring a single-file program into a clean, multi-file structure
* Organizing code into modules by responsibility (separation of concerns)
* Importing specific functions between files with `from x import y`
* Extracting repeated input-validation logic into reusable helpers (DRY)
* Keeping the in-memory data (the inventory list) separate from the file that persists it
* Using `if __name__ == "__main__":` to make a file runnable on its own and safe to import

## Author

**Michael Murchie**

* GitHub: [MichaelTM0](https://github.com/MichaelTM0)
* LinkedIn: [michael-murchie](https://www.linkedin.com/in/michael-murchie/)
