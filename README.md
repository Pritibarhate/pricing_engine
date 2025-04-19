# pricing_engine
# Pricing Engine 📈

This is a simple pricing engine that updates product prices based on inventory levels and recent sales performance.

## 🔧 How it Works

1. Reads data from:
   - `products.csv` — product info (price, cost, stock)
   - `sales.csv` — 30-day sales data

2. Applies pricing rules in priority:
   - Rule 1: Low stock, high demand → increase price 15%
   - Rule 2: Dead stock → decrease price 30%
   - Rule 3: Overstock → decrease price 10%
   - Rule 4: Minimum profit 20% over cost

3. Outputs the final prices in:
   - `updated_prices.csv` with old and new prices.

## 📁 Input Files

| File               | Description                                    |
|--------------------|------------------------------------------------|
| `products.csv`     | Contains SKU, current price, cost, stock       |
| `sales.csv`        | Contains SKU and quantity sold in last 30 days |

## ✅ Output

A new file `updated_prices.csv` with updated prices based on rules.

## 🛠️ How to Run

```bash
python pricing_engine.py
