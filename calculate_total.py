def calculate_total(database):

  
    if not database:
        print('The inventory is empty. Please add a product price')
        return
    
    total = 0
    
    for product in database:

     total += product['quantity'] * product['price']

    print(f'The total value of inventory is: ${total:.2f}')

