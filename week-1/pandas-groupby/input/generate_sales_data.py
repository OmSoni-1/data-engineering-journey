import pandas as pd

header = [
    'order_id', 'order_date', 'customer', 'region', 
    'category', 'product', 'quantity', 'unit_price', 
    'total_amount', 'status'
]

data = [
    # North: High Volume, Lower Avg Value
    [101, '2026-01-05', 'Liam', 'North', 'Peripherals', 'Mouse', 10, 50, 500, 'Completed'],
    [102, '2026-01-12', 'Noah', 'North', 'Peripherals', 'Keyboard', 5, 100, 500, 'Completed'],
    [103, '2026-02-01', 'Oliver', 'North', 'Office', 'Paper', 20, 10, 200, 'Completed'],
    
    # West: High Value Electronics (High Revenue & AOV)
    [104, '2026-01-15', 'Emma', 'West', 'Electronics', 'Laptop', 1, 1200, 1200, 'Completed'],
    [105, '2026-01-20', 'Ava', 'West', 'Electronics', 'Monitor', 2, 400, 800, 'Completed'],
    [106, '2026-02-08', 'Sophia', 'West', 'Electronics', 'Laptop', 1, 1500, 1500, 'Completed'],
    
    # East: Mixed status (Tests your filter)
    [107, '2026-01-10', 'Mia', 'East', 'Office', 'Printer', 1, 300, 300, 'Completed'],
    [108, '2026-01-14', 'James', 'East', 'Electronics', 'Gaming Console', 1, 500, 500, 'Cancelled'], 
    [109, '2025-12-25', 'Lucas', 'East', 'Peripherals', 'Mouse', 2, 50, 100, 'Completed'], 
    
    # South: Bulk Buying
    [110, '2026-01-22', 'Amelia', 'South', 'Peripherals', 'Keyboard', 15, 80, 1200, 'Completed'],
    [111, '2026-02-03', 'Harper', 'South', 'Office', 'Desk Chair', 2, 250, 500, 'Completed'],
    
    # Extra diversified rows
    [112, '2026-01-30', 'Evelyn', 'West', 'Peripherals', 'Headset', 3, 150, 450, 'Completed'],
    [113, '2026-02-07', 'Jack', 'North', 'Electronics', 'Tablet', 1, 600, 600, 'Completed'],
    [114, '2025-11-01', 'Ella', 'South', 'Electronics', 'Laptop', 1, 1000, 1000, 'Completed'], 
    [115, '2026-01-02', 'Henry', 'East', 'Office', 'Shelving', 1, 400, 400, 'Pending']
]

df = pd.DataFrame(data, columns=header)
df.to_csv('sales_data.csv', index=False)

print("Sales data (Day - 2) has been successfuly created!")