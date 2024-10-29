# python-challenge-1
## Menu
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

## Order list to store customer's selections

order_list = []
def add_to_order(menu, category, item, sub_item=None, quantity=1):
    if sub_item:
        price = menu[category][item][sub_item]
        order_list.append({'item_name': f"{sub_item} {item}", 'item_price': price, 'quantity': quantity})
    else:
        price = menu[category][item]
        order_list.append({'item_name': item, 'item_price': price, 'quantity': quantity})


for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

menu_category = input("Enter the menu category: ")



if menu_category.isdigit():
    print("menu_category is a digit.")
else:
    print("error menu_category is not a digit.")


def order_system(menu):
    while True:
        item_category = input("Enter the menu category (e.g., Snacks, Meals, Drinks, Dessert) or type 'exit' to finish: ")
        if item_category.lower() == 'exit':
            break

if item_category not in menu:
            print("Invalid menu category. Please choose a valid option.")
            continue

 item_name = input(f"Enter the item name from the {item_category} menu: ")

if item_name not in menu[item_category]:
            print("Invalid item name. Please choose a valid option.")
            continue

selected_item_name = item_name

 quantity = input(f"Enter the quantity of {selected_item_name} (default is 1 if invalid): ")


if not quantity.isdigit():
            quantity = 1
        else:
            quantity = int(quantity)


add_to_order(menu, item_category, selected_item_name, quantity=quantity)
print(f"{quantity}x {selected_item_name} added to your order.")

# Example usage
order_system(menu_items)

# Print the final order for receipt
print("\nFinal order:")
for item in order_list:
print(item)

def add_to_order(menu, category, item, sub_item=None, quantity=1):
    if sub_item:
        price = menu[category][item][sub_item]
        order_list.append({'Item name': f"{sub_item} {item}", 'Price': price, 'Quantity': quantity})
    else:
        price = menu[category][item]
        order_list.append({'Item name': item, 'Price': price, 'Quantity': quantity})

def order_system(menu):
    place_order = True
    while place_order:
        item_category = input("Enter the menu category (e.g., Snacks, Meals, Drinks, Dessert) or type 'exit' to finish: ")
        if item_category.lower() == 'exit':
            break

if item_category not in menu:
            print("Invalid menu category. Please choose a valid option.")
            continue

 item_name = input(f"Enter the item name from the {item_category} menu: ")

if item_name not in menu[item_category]:
            print("Invalid item name. Please choose a valid option.")
            continue

selected_item_name = item_name

 quantity = input(f"Enter the quantity of {selected_item_name} (default is 1 if invalid): ")
        if not quantity.isdigit():
            quantity = 1
        else:
            quantity = int(quantity)

add_to_order(menu, item_category, selected_item_name, quantity=quantity)
        print(f"{quantity}x {selected_item_name} added to your order.")

       
keep_ordering = input("Would you like to keep ordering? (y/n): ").lower()
            match keep_ordering:
                case 'y':
                    place_order = True
                    break
                case 'n':
                    place_order = False
                    print("Thank you for your order")
                    break
                case _:
                    print("Invalid input. Please type 'y' or 'n'.")

def print_receipt(order_list):
    print("\nOrder Receipt")
    print("--------------------------|--------|----------")
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")
    
item_name = item['Item name']
price = item['Price']
quantity = item['Quantity']
        

spaces = ' ' * (26 - len(item_name))
print(f"{item_name}{spaces}| ${price:.2f} | {quantity}")
    
print("--------------------------|--------|----------")

order_system(menu_items)
print_receipt(order_list)

Developed with the assistance of Copilot   
    
