import os

class VendingMachine:
    def __init__(self):
        # Initialize inventory for drinks, snacks, and sweets
        self.drinks = {
            'D1': {'item': 'Cola', 'price': 1.50, 'quantity': 10},
            'D2': {'item': 'Pepsi', 'price': 1.25, 'quantity': 12},
            'D3': {'item': 'Sprite', 'price': 1.75, 'quantity': 8},
            'D4': {'item': 'Iced Tea', 'price': 1.50, 'quantity': 10},
            'D5': {'item': 'Orange Juice', 'price': 2.00, 'quantity': 8},
            'D6': {'item': 'Apple Juice', 'price': 1.75, 'quantity': 6},
            'D7': {'item': 'Lemonade', 'price': 1.50, 'quantity': 10},
            'D8': {'item': 'Watermelon Juice', 'price': 2.25, 'quantity': 5},
            'D9': {'item': 'Ginger Ale', 'price': 1.50, 'quantity': 8},
            'D10':{'item': 'Cranberry Juice', 'price': 2.00, 'quantity': 7},
        }

        self.snacks = {
            'S1': {'item': 'Potato Chips', 'price': 1.00, 'quantity': 15},
            'S2': {'item': 'Popcorn', 'price': 1.75, 'quantity': 12},
            'S3': {'item': 'Pretzels', 'price': 1.25, 'quantity': 10},
            'S4': {'item': 'Cheese Puffs', 'price': 1.50, 'quantity': 8},
            'S5': {'item': 'Trail Mix', 'price': 2.00, 'quantity': 6},
            'S6': {'item': 'Crispy Tortillas', 'price': 1.75, 'quantity': 9},
            'S7': {'item': 'Nacho Cheese Chips', 'price': 1.50, 'quantity': 11},
            'S8': {'item': 'BBQ Flavored Snack', 'price': 1.75, 'quantity': 7},
            'S9': {'item': 'Chocolate Covered Nuts', 'price': 2.25, 'quantity': 5},
            'S10':{'item': 'Rice Crackers', 'price': 1.25, 'quantity': 13},
        }

        self.sweets = {
            'SW1': {'item': 'Chocolate Bar', 'price': 1.75, 'quantity': 10},
            'SW2': {'item': 'Gummy Bears', 'price': 1.50, 'quantity': 12},
            'SW3': {'item': 'Candy Canes', 'price': 1.25, 'quantity': 15},
            'SW4': {'item': 'Jellybeans', 'price': 1.50, 'quantity': 10},
            'SW5': {'item': 'Milk Chocolate', 'price': 2.00, 'quantity': 8},
            'SW6': {'item': 'Caramel Popcorn', 'price': 2.25, 'quantity': 6},
            'SW7': {'item': 'Marshmallows', 'price': 1.25, 'quantity': 12},
            'SW8': {'item': 'Lollipops', 'price': 1.00, 'quantity': 15},
            'SW9': {'item': 'Fruit Gummies', 'price': 1.75, 'quantity': 10},
            'SW10':{'item': 'Dark Chocolate', 'price': 2.25, 'quantity': 7},
        }

        # Initialize balance
        self.balance = 0.0
        self.purchase_history = []

    def display_category(self, category, items):
        """
        Display items in a specific category.

        Parameters:
        - category: The category name (e.g., 'Drinks')
        - items: Dictionary containing items in the category
        """
        # Display the category heading
        print(f'\n\033[1m{category:^120}\033[0m')
        print('\033[96m' + '\n                                                        ------------------------------------------------------------------------- \033[0m')
        print('\033[93m' + '                                                            (Code)   Item                              Price     Quantity  \033[0m')

        # Get the maximum length of item names for formatting
        max_item_length = max(len(item_info["item"]) for item_info in items.values())

        # Display each item in the category
        for code, item_info in items.items():
            item_name = item_info["item"]
            price = item_info["price"]
            quantity = item_info["quantity"]
            print('\033[92m' + f'                                                            |{code}|     {item_name:<{max_item_length}}                  ${price:<8.2f} {quantity}  \033[0m')
        print('\033[96m' + '                                                        ------------------------------------------------------------------------- \033[0m')

    def display_drinks(self):
        """Display the drinks category."""
        self.display_category('                                                                   Drinks', self.drinks)

    def display_snacks(self):
        """Display the snacks category."""
        self.display_category('                                                                   Snacks', self.snacks)

    def display_sweets(self):
        """Display the sweets category."""
        self.display_category('                                                                   Sweets', self.sweets)

    def enter_money(self):
        """
        Allow the user to enter money and update the balance.
        """
        print('\n\033[1m' + '\033[95m' + '                                                        ============================= Money Entry ===============================\033[0m')
        self.balance = float(input('\033[94m' + '\n                                                                              Enter the amount of money: \033[0m'))
        print('\033[96m' + '                                                        ------------------------------------------------------------------------- \033[0m')

    # ... (previous code)

    def select_item(self, items):
        """
        Allow the user to select an item, purchase it, and update the inventory and balance.

        Parameters:
        - items: Dictionary containing items in the selected category
        """
        code = input('\033[94m' + '\n                                                                  Enter the code of the item you want to purchase: \033[0m')
        
        for category, item_category in {'Drinks': self.drinks, 'Snacks': self.snacks, 'Sweets': self.sweets}.items():
            if code in item_category:
                item_info = item_category[code]
                quantity_to_purchase = int(input('\033[94m' + '\n                                                                       Enter the quantity you want to purchase: \033[0m'))
                print('\033[96m' + '\n                                                        ------------------------------------------------------------------------- \033[0m')
                if item_info['quantity'] >= quantity_to_purchase and self.balance >= item_info['price'] * quantity_to_purchase:
                    # Process the purchase
                    self.balance -= item_info['price'] * quantity_to_purchase
                    item_info['quantity'] -= quantity_to_purchase
                    for _ in range(quantity_to_purchase):
                        self.purchase_history.append(item_info)
                    print('\033[93m' + f'\n                                                                      You purchased {quantity_to_purchase} {item_info["item"]}(s) for ${item_info["price"] * quantity_to_purchase:.2f}.\033[0m')
                    print('\033[96m' + '\n                                                        ------------------------------------------------------------------------- \033[0m')
                    print('\033[91m' + f'\n                                                                              Your remaining balance: ${self.balance:.2f}\033[0m')
                    print('\033[96m' + '\n                                                        ------------------------------------------------------------------------- \033[0m')
                elif item_info['quantity'] < quantity_to_purchase:
                    print('\033[1;31m' + f'\n                                                                  Sorry, there are only {item_info["quantity"]} {item_info["item"]}(s) available.\033[0m')
                    print('\033[96m' + '\n                                                        ------------------------------------------------------------------------- \033[0m')

                else:
                    print('\033[96m' + '\n                                                        ------------------------------------------------------------------------- \033[0m')
                    print('\033[1;31m' +'\n                                                                                    Insufficient funds. \n                                                                                   Please add more money.\033[0m')
                    print('\033[96m' + '\n                                                        ------------------------------------------------------------------------- \033[0m')
                return
        print('\033[96m' + '\n                                                        ------------------------------------------------------------------------- \033[0m')
        print('\033[1;31m' + '\n                                                                                      Invalid code.\n                                                                                    Please try again.\033[0m')
        print('\033[96m' + '\n                                                        ------------------------------------------------------------------------- \033[0m')

# ... (remaining code)


    def return_change(self):
        """
        Display the remaining balance as change when the user exits.
        """
        print('\n\033[1m' + '\033[95m' + '                                                        ============================= Return Change ===============================\033[0m')
        print('\033[91m' + f'\n                                                                                   Change returned: ${self.balance:.2f}\033[0m')
        print('\033[96m' + '\n                                                        ------------------------------------------------------------------------- \033[0m')
        self.display_bill()

    def display_bill(self):
        """
        Display the bill with the items purchased and total money used.
        """
        print('\n\033[1m' +'\033[95m' + '                                                        ============================= Purchase Bill ===============================\033[0m')
        total_money_used = 0
        for item in self.purchase_history:
            item_name = item["item"]
            price = item["price"]
            total_money_used += price
            print('\033[92m' + f'\n                                                                          Item: {item_name} | Price: ${price:.2f}\033[0m')
        print('\033[95m' + '                                                        =========================================================================== \033[0m')
        print('\033[93m' + f'\n                                                                                 Total Money Used: ${total_money_used:.2f}\033[0m')
        print('\033[95m' + '\n                                                        =========================================================================== \033[0m')

    def display_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print('\033[1;31m' + '===========================================================================================================================================================================================\033[0m')
        print('\033[1;31m' + '            :::        ::: :::::::::: ::::    ::: :::::::::  ::::::::::: ::::    :::  ::::::::   ::::    ::::      :::      ::::::::  :::    ::: ::::::::::: ::::    ::: ::::::::::        \033[0m')
        print('\033[1;31m' + '            :+:        :+: :+:        :+:+:   :+: :+:    :+:     :+:     :+:+:   :+: :+:    :+:  +:+:+: :+:+:+   :+: :+:   :+:    :+: :+:    :+:     :+:     :+:+:   :+: :+:               \033[0m')  
        print('\033[1;31m' + '            +:+        +:+ +:+        :+:+:+  +:+ +:+    +:+     +:+     :+:+:+  +:+ +:+         +:+ +:+:+ +:+  +:+   +:+  +:+        +:+    +:+     +:+     :+:+:+  +:+ +:+               \033[0m')
        print('\033[1;31m' + '             +#+       +:+ +#++:++#   +#+ +:+ +#+ +#+    +:+     +#+     +#+ +:+ +#+ :#:         +#+  +:+  +#+ +#++:++#++: +#+        +#++:++#++     +#+     +#+ +:+ +#+ +#++:++#          \033[0m')
        print('\033[1;31m' + '               +#+   +#+   +#+        +#+  +#+#+# +#+    +#+     +#+     +#+  +#+#+# +#+   +#+#  +#+       +#+ +#+     +#+ +#+        +#+    +#+     +#+     +#+  +#+#+# +#+               \033[0m')
        print('\033[1;31m' + '                #+#+#+#    #+#        #+#   #+#+# #+#    #+#     #+#     #+#   #+#+# #+#    #+#  #+#       #+# #+#     #+# #+#    #+# #+#    #+#     #+#     #+#   #+#+# #+#               \033[0m')
        print('\033[1;31m' + '                  ###      ########## ###    #### #########  ########### ###    ####  ########   ###       ### ###     ###  ########  ###    ### ########### ###    #### ##########        \033[0m')
        print('\033[1;31m' + '===========================================================================================================================================================================================\033[0m')

        # Display category options
        print('\033[96m' + '                                                        ------------------------------------------------------------------------- \033[0m')
        print('\033[92m' + '                                                                                    Choose a category')
        print('\033[92m' +'                                                                                    1. Drinks')
        print('\033[92m' +'                                                                                    2. Snacks')
        print('\033[92m' +'                                                                                    3. Sweets')
        print('\033[92m' +'                                                                                    0. Exit\033[0m')
        print('\033[96m' + '                                                        ------------------------------------------------------------------------- \033[0m')

    def vending_machine_interface(self):
        """
        Main interface for the vending machine.
        """
        self.display_menu()  # Display the vending machine title and category options
        while True:
            option = input('\033[94m' + '                                                                                    Enter the number: \033[0m')
            print('\033[96m' + '                                                        ------------------------------------------------------------------------- \033[0m')
            if option == '0':
                # Exit the vending machine and return change
                self.return_change()
                break
            elif option == '1':
                # Display drinks, allow money entry, and item selection
                self.display_drinks()
                self.enter_money()
                self.select_item(self.drinks)
            elif option == '2':
                # Display snacks, allow money entry, and item selection
                self.display_snacks()
                self.enter_money()
                self.select_item(self.snacks)
            elif option == '3':
                # Display sweets, allow money entry, and item selection
                self.display_sweets()
                self.enter_money()
                self.select_item(self.sweets)
            else:
                        print('\033[1;31m' + '\n                                                                                      Invalid option.\n                                                                                    Please try again.\033[0m')
                        print('\033[96m' + '\n                                                        ------------------------------------------------------------------------- \033[0m')



if __name__ == "__main__":
    # Instantiate the vending machine and start the interface
    vending_machine = VendingMachine()
    vending_machine.vending_machine_interface()