# HEROES.py - Hero list management (functional style)

def display_heroes(heroes):
    """Display the current list of heroes."""
    print("Heroes:", heroes)


def add_hero(heroes, hero):
    """Add a hero to the end of the list."""
    heroes.append(hero)


def insert_hero(heroes, index, hero):
    """Insert a hero at a specific position."""
    heroes.insert(index, hero)


def remove_hero(heroes, hero):
    """Remove a hero from the list if it exists."""
    if hero in heroes:
        heroes.remove(hero)
    else:
        print(f"'{hero}' not found in the list.")


def display_sorted_heroes(heroes, descending=False):
    """Display heroes sorted ascending (default) or descending."""
    order = "Descending" if descending else "Ascending"
    print(f"Heroes sorted ({order}):", sorted(heroes, reverse=descending))


def main():
    heroes = ['Ironman', 'Thor', 'Hulk', 'Spiderman']

    # 1. Display heroes
    display_heroes(heroes)

    # 2. Add a hero
    add_hero(heroes, 'Black Panther')
    display_heroes(heroes)

    # 3. Insert a hero at a specific position
    insert_hero(heroes, 1, 'Cpt. America')
    display_heroes(heroes)

    # 4. Remove a hero
    remove_hero(heroes, 'Spiderman')
    display_heroes(heroes)

    # 5. Display sorted heroes (Ascending / Descending)
    display_sorted_heroes(heroes)
    display_sorted_heroes(heroes, descending=True)


main()
