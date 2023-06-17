import mysql.connector

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(
    host='47.242.43.132',  # Replace with your MySQL host
    user='root',  # Replace with your MySQL username
    password='dsfwer@#$23fdsff3245',  # Replace with your MySQL password
    database='rakutencon'  # Replace with your MySQL database name
)

# Create a cursor object
cursor = cnx.cursor()

create_table_query = """
CREATE TABLE zag_product_inventory_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_code VARCHAR(100) NOT NULL,
    in_stock BOOLEAN NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

cursor.execute(create_table_query)

cnx.commit()

cursor.close()
cnx.close()