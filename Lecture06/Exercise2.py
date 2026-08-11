# Exercise2.py - Inventory management with lists and functions

def update_inventory(inventory, item_name, quantity_sold):
    """Reduce the quantity of a specified item after a sale."""
    for i, (name, quantity, price) in enumerate(inventory):
        if name == item_name:
            new_quantity = quantity - quantity_sold
            # Tuples are immutable, so replace the whole record
            inventory[i] = (name, new_quantity, price)
            print(f"Sold {quantity_sold} {item_name}(s). New quantity: {new_quantity}")
            return
    print(f"'{item_name}' not found in inventory.")


def calculate_total_value(inventory):
    """Return the total value of all items in stock."""
    total = 0.0
    for name, quantity, price in inventory:
        total += quantity * price
    return total


def find_most_expensive(inventory):
    """Return the name of the item with the highest unit price."""
    most_expensive = inventory[0][0]
    highest_price = inventory[0][2]
    for name, quantity, price in inventory:
        if price > highest_price:
            highest_price = price
            most_expensive = name
    return most_expensive


def add_item(inventory, item_name, quantity, price):
    """Add a new item, or update the quantity/price of an existing one."""
    for i, (name, old_quantity, old_price) in enumerate(inventory):
        if name == item_name:
            inventory[i] = (item_name, quantity, price)
            print(f"Updated '{item_name}' to {quantity} units @ ${price:.2f}")
            return
    inventory.append((item_name, quantity, price))
    print(f"Added '{item_name}': {quantity} units @ ${price:.2f}")


def display_inventory(inventory):
    """Print the full inventory as a table."""
    print("Current inventory:")
    for name, quantity, price in inventory:
        print(f"  {name:8s} {quantity:4d} units @ ${price:.2f}")


def main():
    inventory = [
        ("Apple", 50, 0.75),
        ("Banana", 100, 0.50),
        ("Orange", 75, 0.80),
    ]

    # 1. Update inventory after selling 20 bananas
    update_inventory(inventory, "Banana", 20)

    # 2. Calculate the total value of the inventory
    total_value = calculate_total_value(inventory)
    print(f"Total inventory value: ${total_value:.2f}")

    # 3. Find the most expensive item
    print(f"Most expensive item: {find_most_expensive(inventory)}")

    # 4. Add "Eggs" with 30 units @ $0.25, then update it to 50 units @ $0.30
    add_item(inventory, "Eggs", 30, 0.25)
    add_item(inventory, "Eggs", 50, 0.30)

    # Show the final inventory
    display_inventory(inventory)


main()
