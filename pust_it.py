import sqlite3

# Connect to test.db
conn1 = sqlite3.connect('db_5test.db')
c1 = conn1.cursor()

# Connect to db.sqlite3
conn2 = sqlite3.connect('db.sqlite3')
c2 = conn2.cursor()

# Get all rows from Product_5arms table
c1.execute("SELECT * FROM Product_5arms")
rows = c1.fetchall()

# Insert rows into product_product table
for row in rows:
    c2.execute("INSERT INTO product_product VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)

# Commit changes and close connections
conn2.commit()
conn1.close()
conn2.close()

print("Rows successfully added from Product_5arms to product_product.")