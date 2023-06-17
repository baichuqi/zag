import mysql.connector
from mysql.connector import Error

class MySQL():
    def __init__(self, table) -> None:
        # Establish a connection to the MySQL database
        self.cnx = mysql.connector.connect(
            host='47.242.43.132',  # Replace with your MySQL host
            user='root',  # Replace with your MySQL username
            password='dsfwer@#$23fdsff3245',  # Replace with your MySQL password
            database=table  # Replace with your MySQL database name
        )

        # Create a cursor object
        self.cursor = self.cnx.cursor()

    def get_item_from_table(self, table_name):
        query = f'SELECT * FROM {table_name}'
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def insert_into_product_inventory(self, data):
        try:
            insert_query = """
            INSERT INTO zag_product_inventory_history (item_code, in_stock, price)
            VALUES (%s, %s, %s)
            """
            self.cursor.executemany(insert_query, data)
            self.cnx.commit()

        except Error as e:
            print("insert error", e)  
        finally:
            if self.cursor or self.cnx:
                self.close()  

    def close(self):
        # Close the cursor and connection
        self.cursor.close()
        self.cnx.close()


# rakutencon = MySQL('rakutencon')
# items = [
#     ('test_code:1111', 1, 34.5),
#     ('test_code:2222', 0, 33.5),
# ]
# rakutencon.insert_into_product_inventory(items)
# items = rakutencon.get_item_from_table('aucbreakout_item')
# print(len(items))