import csv

# Step 1: Read product data from products.csv
with open('products.csv', newline='') as f:
    reader = csv.DictReader(f)
    products = list(reader)

# Step 2: Read sales data from sales.csv
sales = {}
with open('sales.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        sales[row['sku']] = int(row['quantity_sold'])

# Step 3: Process data for pricing
updated_prices = []
for product in products:
    sku = product['sku']
    old_price = float(product['current_price'])
    cost = float(product['cost_price'])
    stock = int(product['stock'])
    sold = sales.get(sku, 0)  # If no sales data, assume 0 sales
    new_price = old_price

    # Rule 1: Low Stock, High Demand
    if stock < 20 and sold > 30:
        new_price = old_price * 1.15
    # Rule 2: Dead Stock
    elif stock > 200 and sold == 0:
        new_price = old_price * 0.7
    # Rule 3: Overstocked Inventory
    elif stock > 100 and sold < 20:
        new_price = old_price * 0.9

    # Rule 4: Minimum Profit Constraint
    if new_price < cost * 1.2:
        new_price = cost * 1.2

    # Add to updated list
    updated_prices.append([sku, round(old_price, 2), round(new_price, 2)])

# Step 4: Write the updated prices to updated_prices.csv
with open('updated_prices.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["sku", "old_price (in USD)", "new_price (in USD)"])  # Header
    writer.writerows(updated_prices)

print("Updated prices saved in 'updated_prices.csv'")
