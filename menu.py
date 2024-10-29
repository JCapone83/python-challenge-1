# Menu dictionary
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

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1
        
    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number

    if menu_category.isdigit():
         
        # Check if the customer's input is a valid option
         if int(menu_category) in menu_items.keys():


            # 2. Ask customer to input menu item number

item_number = input("Enter the menu item number: ")

            # 3. Check if the customer typed a number

if not item_number.isdigit():


                # Convert the menu selection to an integer

item_number = int(item_number)

                # 4. Check if the menu selection is in the menu items

if int(menu_category) in menu_items.keys():


                    # Store the item name as a variable

 menu_category_name = menu_items[int(menu_category)]

                    # Tell the customer that their input isn't valid

print("The menu item you selected is invalid.")

                # Tell the customer they didn't select a menu option
def add_to_order(menu, category, item, sub_item=None, quantity=1):
    if sub_item:
        price = menu[category][item][sub_item]
        order_list.append({'Item name': f"{sub_item} {item}", 'Price': price, 'Quantity': quantity})
    else:
        price = menu[category][item]
        order_list.append({'Item name': item, 'Price': price, 'Quantity': 
def order_system(menu):
    place_order = True
    while place_order:
        item_category = input("Enter the menu category (e.g., Snacks, Meals, Drinks, Dessert) or type 'exit' to finish: ")
        if item_category.lower() == 'exit':
            break

        if item_category not in menu:
            print("Invalid menu category. Please choose a valid option.")   
            # Tell the customer they didn't select a menu option
        
  item_name = input(f"Enter the item name from the {item_category} menu: ")

        # Tell the customer they didn't select a number

            def get_number_from_user():
    try:
        number = float(input("Please enter a number: "))
        return number
    except ValueError:
        print("It looks like you didn't select a number. Please try again.")


        # Ask the customer if they would like to order anything else
def ask_if_customer_wants_more():
    response = input("Would you like anything else? (yes/no): ").strip().lower()
    if response == "yes":
        print("Good! What else can I get for you?")
    elif response == "no":
        print("Thank you! Let me know if there's anything else later.")
    else:
        print("I didn't understand that. Please enter 'yes' or 'no'.")

        # 5. Check the customer's input
def get_yes_no_response():
    response = input("Would you like anything else? (yes/no): ").strip().lower()
    if response == "yes":
        return True
    elif response == "no":
        return False
    else:
        print("I didn't understand that. Please enter 'yes' or 'no'.")
        
        return get_yes_no_response()  # Re-prompt if the input is unclear
                # Keep ordering
keep_ordering = input("Would you like to keep ordering? (y/n): ").lower() match keep_ordering: case 'y': place_order = True break case 'n': place_order = False 
print("Thank you for your order") break case _: 
print("Invalid input. Please type 'y' or 'n'.")
                # Exit the keep ordering question loop

choice = input("\nWhat would you like to order? (Enter 'done' when finished or 'exit' to cancel): ").strip().lower()


            return  # Exit the function to end the process
                # Complete the order
 confirm = input("\nWould you like to complete this order? (yes/no): ").strip().lower()
        if confirm == "yes":
            print("Thank you! Your order has been completed.")
        else:
            print("Order canceled. Let us know if you need anything else.")
    else:
        print("No items ordered. Let us know if you need anything.")
        
                # Since the customer decided to stop ordering, thank them for
                # their order
                print("Thank you for your order.")

                # Exit the keep ordering question loop
  if choice == 'exit':
            print("Order canceled. Thank you, and have a nice day!")

                # Tell the customer to try again
print(f'{keep_ordering} is not a valid input.')

# Print out the customer's order

if len(order_list) > 0:
    print("Customer order finished:\n")
    for item in order_list:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]
        print(f"{quantity} x {item_name} at ${price:.2f} each")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

for items in order_list:
     
    # 7. Store the dictionary items as variables
item1 = {'Item name': 'Apple', 'Price': 0.49, 'Quantity': 1}
item2 = {'Item name': 'Tea - Thai iced', 'Price': 3.99, 'Quantity': 2}
item3 = {'Item name': 'Fried banana', 'Price': 4.49, 'Quantity': 3}

# Order list
order_list = [item1, item2, item3]

    # 8. Calculate the number of spaces for formatted printing

         item_name_spaces = 26 - len(item_name)
            Price_space = 8 - len(str(Price))
            quantity_space = 10 - len(str(quantity))
    # 9. Create space strings
menu = "Menu"
spaced_menu = " ".join("Menu")
print(spaced_menu)

    # 10. Print the item name, price, and quantity

print(f"{str(item_name)}{' ' * item_name_spaces}|{str(Price)}{' ' * Price_space}|{str(quantity)}{' ' * quantity_space}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.

cost_of_order =  sum([int(items["quantity"])* float(items["price"]) for items in order_list])
        print(f"Your amount due is ${cost_of_order}")



Work aided by ChatGPT & CoPilot
