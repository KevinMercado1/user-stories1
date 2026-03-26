from add_product import add_product
from calculate_total import calculate_total
from show_inventory import show_inventory

database = []


def menu ():
   
    x = True
    while x:
            print('\n --- Menu Options ---\n')
            print('1.Add Products')
            print('2.Calculate Total')
            print('3.Show Inventory')
            print('4.Exit')

            option = input('Please enter a option: ')

            if option == '1':
                add_product(database)

            elif option == '2':
                calculate_total(database)
                
            elif option == '3':
                 show_inventory(database)

            elif option == '4':
                print('Thanks For Coming')
                x = False


if __name__ == "__main__": 
    menu()