def display_inventory(vehicles):
    """Display the current inventory of vehicles"""
    # This function prints all vehicles in the inventory list.
    # If the inventory is empty, it notifies the user.
    if not vehicles:
        print("\nInventory is empty!")
        return
    
    print("\nCurrent Inventory:")
    print("------------------")
    for idx, vehicle in enumerate(vehicles, 1):
        print(f"{idx}. VIN: {vehicle['vin']}")
        print(f"   Make: {vehicle['make']}")
        print(f"   Model: {vehicle['model']}")
        print(f"   Year: {vehicle['year']}")
        print(f"   Status: {vehicle['status']}")
        print("------------------")

def add_vehicle(vehicles):
    """Add a new vehicle to the inventory"""
    # This function prompts the user for vehicle details and adds a new vehicle to the inventory.
    # It checks for duplicate VINs before adding.
    vin = input("Enter VIN: ")
    
    # Check if VIN already exists
    for vehicle in vehicles:
        if vehicle['vin'] == vin:
            print("Error: VIN already exists in inventory!")
            return
    
    # Collect vehicle details
    make = input("Enter make: ")
    model = input("Enter model: ")
    year = input("Enter year: ")
    
    # Add new vehicle to inventory
    vehicles.append({
        'vin': vin,
        'make': make,
        'model': model,
        'year': year,
        'status': 'Available'
    })
    print("Vehicle added successfully!")

def search_vehicles(vehicles):
    """Search vehicles by make and model"""
    # This function allows the user to search for vehicles by make and/or model.
    # It prints all vehicles that match the search criteria.
    search_make = input("Enter make to search (or press Enter to skip): ").lower()
    search_model = input("Enter model to search (or press Enter to skip): ").lower()
    
    found_vehicles = []
    
    # Nested loop for searching with multiple criteria
    for vehicle in vehicles:
        matches_make = not search_make or vehicle['make'].lower() == search_make
        matches_model = not search_model or vehicle['model'].lower() == search_model
        
        if matches_make and matches_model:
            found_vehicles.append(vehicle)
    
    if found_vehicles:
        print("\nFound Vehicles:")
        for idx, vehicle in enumerate(found_vehicles, 1):
            print(f"{idx}. VIN: {vehicle['vin']} - {vehicle['make']} {vehicle['model']} ({vehicle['year']})")
    else:
        print("\nNo vehicles found matching the criteria.")

def main():
    # Main function to run the vehicle inventory management system.
    # Initializes the inventory and displays the menu loop.
    inventory = [
        {
            'vin': '1HGCM82633A004352',
            'make': 'Honda',
            'model': 'Accord',
            'year': '2020',
            'status': 'Available'
        }
    ]
    
    while True:
        print("\nVehicle Inventory Management System")
        print("1. Display Inventory")
        print("2. Add Vehicle")
        print("3. Search Vehicles")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            add_vehicle(inventory)
        elif choice == '3':
            search_vehicles(inventory)
        elif choice == '4':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    # Entry point for the program
    main()