def show_inventory(database):
    # Check if the database has any items
    if not database:
        print("\n[!] The inventory is empty.")
        return 
    
    total_inventory_value = 0
    total_units = 0

    # Print table header with formatting
    print(f"\n{'PRODUCT':<15} | {'QUANTITY':<10} | {'PRICE':<10} | {'SUBTOTAL':<10}")
    print("-" * 55)

    for product in database:
        name = product['name']
        qty = product['quantity']
        price = product['price']

        # Calculate subtotal for each product row
        subtotal = qty * price

        total_units += qty
        total_inventory_value += subtotal
        
        # Display formatted product details
        print(f"{name:<15} | {qty:<10} | ${price:<9.2f} | ${subtotal:<9.2f}")

    # Display final summary and totals
    print("-" * 55)
    print(f"{'TOTALS':<15} | {total_units:<10} | ${total_inventory_value:<9.2f}")

    # Wait for user input before clearing the view
    input("\nPress Enter to return to menu...")