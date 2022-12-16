import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f'{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}'


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============

#Reads show data from file and adds it to shoe_list
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as f:
            next(f)
            for line in f:
                attribute_list = line.split(',')
                shoe_list.append(Shoe(attribute_list[0], attribute_list[1], attribute_list[2], attribute_list[3], attribute_list[4]))
    except FileNotFoundError as error:
        print(f'{error}: There is currently no inventory.')

#Adds a new show to the shoe list
def capture_shoes():
    country = input('Enter country: ')
    code = input('Enter code: ')
    product = input('Enter product: ')
    cost = input('Enter cost: ')
    quantity =  input('Enter quantity: ')
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    print('Success: Shoe stored!')

#Prints all the data of each shoe
def view_all():
    for item in shoe_list:
        print(item)

#Finds the shoe with the lowest quantity and allows a restock - which is then updated on the inventory.txt file
def re_stock():
    index = 0
    value = shoe_list[0].quantity
    for count, item in enumerate(shoe_list, start = 0):
        if item.quantity < value:
            index = count
            value = item.quantity
    print(f'Lowest quantity: {shoe_list[index].product}, {shoe_list[index].quantity} shoes')
    user_choice = input('Do you wish to restock this item (Y/N)? ').upper()
    if user_choice == 'Y':
        add = int(input('Enter how many more are being added: '))
        shoe_list[index].quantity += add
        new_file = 'Country,Code,Product,Cost,Quantity'
        with open('inventory.txt', 'r') as f:
            for line in f:
                new_line = line.split(',')
                if new_line[1] == shoe_list[index].code:
                    new_line[4] += add
                new_file += '\n' + ','.join(new_line)
        with open('inventory.txt', 'w') as f:
            f.write(new_file)
        print('Quantity updated.')
    else:
        print('Quantity not updated.')

#Allows a user to search for a specific shoe
def search_shoe():
    returned = False
    code = input('\nEnter shoe code: ')
    for item in shoe_list:
        if item.code == code:
            print(f'\n{item}')
            returned = True
    if returned == False:
        print('\nCode does not exist.')

#Calculates total value for each product and prints it
def value_per_item():
    print('Total Value for all products:\n')
    for item in shoe_list:
        print(f'{item.product}: ${int(item.quantity) * int(item.cost)}')

#Finds highest quantity shoe and puts it on sale
def highest_qty():
    index = 0
    value = shoe_list[0].quantity
    for count, item in enumerate(shoe_list, start = 0):
        if item.quantity > value:
            index = count
            value = item.quantity
    print(f'\n{shoe_list[index].product} is on sale!')

#==========Main Menu=============
read_shoes_data()

while True:
    user_input = input('''
                        MENU
___________________________________________________________
cs  - capture shoe
va  - view all
rs  - restock
ss  - search shoe
vpi - value per item
hq  - highest quantity
q   - quit
___________________________________________________________
:''')
    if user_input == 'cs':
        capture_shoes()
    elif user_input == 'va':
        view_all()
    elif user_input == 'rs':
        re_stock()
    elif user_input == 'ss':
        search_shoe()
    elif user_input == 'vpi':
        value_per_item()
    elif user_input == 'hq':
        highest_qty()
    elif user_input == 'q':
        print('\nGoodbye!')
        break
    else:
        print('\nInvalid input. Please try again.\n')