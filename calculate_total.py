def calculate_total(database):

    # Check if the database is empty before calculating
    if not database:
        print('The inventory is empty. Please add a product price')
        return
    
    total = 0
    
    # Iterate through the database to calculate the total value
    for product in database:
        # Multiply quantity by price for each item
        total += product['quantity'] * product['price']

    # Display the formatted total inventory value
    print(f'The total value of inventory is: ${total:.2f}')