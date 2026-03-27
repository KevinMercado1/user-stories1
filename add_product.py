def add_product(database):
    n = True
    while n:
        # Get product name from user
        prod = input('Please enter a product: ').lower()

        while n:
            try:
                # Validate quantity as a positive integer
                qty = int(input('Enter quantity: '))
                if qty <= 0: print('Enter a valid number')
                else: break
            except ValueError: print('Only allow number.')

        while n: 
            try:
                # Validate price as a positive float
                price = float(input('Enter the price: '))
                if price <= 0: print('Only can be enter numbers!')
                else: break
            except ValueError: print('Cannot contain letters.')

        # Create dictionary and append to database
        new__prod = {'name': prod, 'quantity': qty, 'price': price}
        database.append(new__prod)
        print('\nAdding successfully!\n')

        # Check if the user wants to add more items
        again = input('Do you want to add another product? (y/n): ').lower()
        if again != 'y':
            n = False