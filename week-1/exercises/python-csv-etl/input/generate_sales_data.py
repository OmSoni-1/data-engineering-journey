import pandas as pd

header = ['order_id', 'order_date', 'customer', 'product', 'amount', 'status']
data = [
    [101, '2026-01-13', 'Alexa', 'Gaming Console', 2500, 'Completed'],
    [102, '2026-02-12', 'Alice', 'Keyboard', 1200, 'Completed'],
    [103, '2026-01-15', 'Bob', 'Mouse', 800, 'Pending'],
    [104, '2025-11-20', 'Charlie', 'Monitor', 3000, 'Completed'],
    [105, '2026-01-25', 'David', 'Laptop', 5000, 'Cancelled'],
    [106, '2025-12-30', 'Eve', 'Printer', 1500, 'Completed']
]

df = pd.DataFrame(data, columns=header)
df.to_csv('sales_data.csv', index=False)

print('Sales Data CSV successfully created!')