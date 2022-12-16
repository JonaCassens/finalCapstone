# Shoe Inventory Management System
This is a Python program that allows users to manage an inventory of shoes. The program includes functions to read shoe data from a file, add new shoes to the inventory, view all shoes in the inventory, restock a shoe with the lowest quantity, search for a specific shoe, calculate the total value for each product, put the shoe with the highest quantity on sale, and exit the program.

## Getting Started
To use this program, clone or download the repository to your local machine and make sure you have Python installed.

## Usage
Run the program using *python shoe_inventory.py* in the command line. The program will prompt you with a menu of options:

1.Read shoes data from file
2.Capture shoes
3.View all shoes
4.Restock shoe with lowest quantity
5.Search for shoe
6.Calculate value per item
7.Put highest quantity shoe on sale
8.Exit

Select an option by entering the corresponding number and follow the prompts.

## Class Definitions
The *Shoe* class stores information about a shoe, including its country of origin, code, product name, cost, and quantity. It has a *get_cost* and *get_quantity* method to return the cost and quantity of the shoe, respectively, and a *___str__* method to return a string representation of the shoe's attributes.

## File Information
The program reads shoe data from the *inventory.txt* file, which should be in the same directory as the *shoe_inventory.py* file. The file should be in the following format, with each attribute separated by a comma:

Country,Code,Product,Cost,Quantity

Any changes made to the inventory are also updated in the inventory.txt file.

## Additional Notes
The *read_shoes_data* function will return a *FileNotFoundError* if the *inventory.txt* file is not found.
The *capture_shoes*, *re_stock*, and *search_shoe* functions require user input.
The *highest_qty* function puts the shoe with the highest quantity on sale by reducing its cost by 20%.
