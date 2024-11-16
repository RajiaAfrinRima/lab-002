# Smartphone Inventory Management Trading Agent

# Parameters
average_price = 600  # Average price of the smartphone model
price_discount_threshold = 0.8 * average_price  # 20% discount threshold
critical_stock_level = 10  # Minimum stock level to trigger immediate order
minimum_order_quantity = 10  # Minimum units to restock
regular_order_quantity = 15  # Quantity to order during discounts

# Function to determine order quantity
def decide_order(current_price, amount_in_stock):
    """
    Determines the quantity of smartphones to order based on price and stock levels.
    
    Parameters:
        current_price (float): Current price of the smartphone model.
        amount_in_stock (int): Current stock level of the smartphone model.
        
    Returns:
        int: The quantity to order (tobuy).
    """
    if current_price <= price_discount_threshold:  # Price is discounted
        if amount_in_stock < critical_stock_level:  # Stock is critically low
            return minimum_order_quantity
        else:  # Stock is not critically low
            return regular_order_quantity
    elif amount_in_stock < critical_stock_level:  # Stock is critically low
        return minimum_order_quantity
    else:  # No action needed
        return 0

# Simulate agent's decision-making process
def simulate_agent(current_price, amount_in_stock):
    """
    Simulates the agent's decision-making process and prints the result.
    
    Parameters:
        current_price (float): Current price of the smartphone model.
        amount_in_stock (int): Current stock level of the smartphone model.
    """
    print(f"Current Price: {current_price}")
    print(f"Stock Level: {amount_in_stock}")
    
    tobuy = decide_order(current_price, amount_in_stock)
    if tobuy > 0:
        print(f"Decision: Order {tobuy} units.")
    else:
        print("Decision: No order needed.")

# Example Scenarios
scenarios = [
    {"current_price": 500, "amount_in_stock": 20},  # Price Drop & Adequate Stock
    {"current_price": 600, "amount_in_stock": 8},   # Price Stable & Critical Stock
    {"current_price": 600, "amount_in_stock": 25},  # Price Stable & Adequate Stock
    {"current_price": 500, "amount_in_stock": 5},   # Price Drop & Critical Stock
]

# Run scenarios
for i, scenario in enumerate(scenarios, start=1):
    print(f"\nScenario {i}:")
    simulate_agent(scenario["current_price"], scenario["amount_in_stock"])
