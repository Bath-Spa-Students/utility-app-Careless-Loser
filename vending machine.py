import os
class VendingMachine:
    def __init__(self):
        self.inventory = {
            'Drinks': {
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
            },
            'Snacks': {
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
            },
            'Sweets': {
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
        }
        self.balance = 0.0

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

        for category, items in self.inventory.items():
            print('\033[1m' + f'\n                                   {category:^120}\033[0m')
            print('\033[95m' + '                                                        -----------------------------------------------------------------------------  \033[0m')
            print('\033[93m' + '                                                                      (Code)   Item                    Price    Quantity  \033[0m')

            # Get the maximum length of item names for formatting
            max_item_length = max(len(item_info["item"]) for item_info in items.values())

            for code, item_info in items.items():
                item_name = item_info["item"]
                price = item_info["price"]
                quantity = item_info["quantity"]
                print('\033[92m' + f'                                                                      ({code})     {item_name:<{max_item_length}}  ${price:<8.2f}  {quantity}\033[0m')
            print('\033[95m' + '                                                        -------------------------------------------------------------------------------- \033[0m')

    def enter_money(self):
        print('\n\033[1m' + '\033[94m' + '================================ Money Entry ================================\033[0m')
        self.balance = float(input('Enter the amount of money: '))

    def select_item(self):
        code = input('Enter the code of the item you want to purchase: ')
        for category, items in self.inventory.items():
            if code in items:
                item_info = items[code]
                if item_info['quantity'] > 0 and self.balance >= item_info['price']:
                    self.balance -= item_info['price']
                    item_info['quantity'] -= 1
                    print(f'\nYou purchased {item_info["item"]} for ${item_info["price"]:.2f}.')
                    print(f'Your remaining balance: ${self.balance:.2f}')
                elif item_info['quantity'] == 0:
                    print('Sorry, this item is out of stock.')
                else:
                    print('Insufficient funds. Please add more money.')
                return
        print('Invalid code. Please try again.')

    def return_change(self):
        print('\n\033[1m' + '\033[94m' + '=============================== Return Change ===============================\033[0m')
        print(f'Change returned: ${self.balance:.2f}')

    def vending_machine_interface(self):
        while True:
            self.display_menu()
            print('(0) Exit')
            option = input('Choose an option: ')

            if option == '0':
                self.return_change()
                break
            elif option == '1':
                self.enter_money()
            elif option == '2':
                self.select_item()
            else:
                print('Invalid option. Please try again.')

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.vending_machine_interface()