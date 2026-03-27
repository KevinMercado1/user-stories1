from add_product import add_product
from calculate_total import calculate_total
from Show_inventory import show_inventory

# Initialize the global inventory list
database = []

def menu():
   
    x = True
    while x:
            # Display the main menu to the user
            print('\n --- Menu Options ---\n')
            print('1.Add Products')
            print('2.Calculate Total')
            print('3.Show Inventory')
            print('4.Exit')

            option = input('Please enter a option: ')

            # Route to the selected function based on user input
            if option == '1':
                add_product(database)

            elif option == '2':
                calculate_total(database)
                
            elif option == '3':
                 show_inventory(database)

            # Exit the program loop
            elif option == '4':
                print('Thanks For Coming')
                x = False

# Program entry point
if __name__ == "__main__": 
    menu()