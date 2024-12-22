def add_to_menu(menu, item):
    menu.append(item)
    return menu

def remove_from_menu(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} does not exist in the menu.")
    return menu

def check_for_availability(menu, item):
    if item in menu:
        return f"{item} is available"
    else:
        return f"{item} is not available"

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"

updated_menu = add_to_menu(initial_menu, add_item)
updated_menu = remove_from_menu(updated_menu, remove_item)
availability = check_for_availability(updated_menu, check_item)

print(f"Updated Menu: {updated_menu}")
print(f"Availability: {availability}")
