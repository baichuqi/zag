import mysql.connector
from mysql.connector import Error


class MySQL():
    def __init__(self, database) -> None:
        # Establish a connection to the MySQL database
        self.cnx = mysql.connector.connect(
            host='18.179.195.219',  # Replace with your MySQL host
            user='zag_shop',  # Replace with your MySQL username
            port='3308',
            password='DYr36i3P5Bz2Mzpj',  # Replace with your MySQL password
            database=database  # Replace with your MySQL database name
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
            INSERT INTO zag_product_inventory_history (product_id, is_available, price, is_take_off, take_off_time, update_time)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.cursor.executemany(insert_query, data)
            self.cnx.commit()
            print("insert successful")
        except Error as e:
            print("insert error", e)  
        finally:
            if self.cursor or self.cnx:
                self.close()  
    def backup_product_inventory(self):
        try:
            insert_query = """
            INSERT INTO zag_product_inventory_history_bk (product_id, is_available, price, is_take_off, take_off_time, update_time)
            SELECT product_id, is_available, price, is_take_off, take_off_time, update_time from zag_product_inventory_history
            """
            self.cursor.execute(insert_query)
            self.cnx.commit()
            print("backup successfully")
        except Error as e:
            print("backup insert error")
        finally:
            print("clear table zag_product_inventory_history data")
            self.cursor.execute("DELETE FROM zag_product_inventory_history")
            self.cnx.commit()
            if self.cursor or self.cnx:
                self.close()

    def close(self):
        # Close the cursor and connection
        self.cursor.close()
        self.cnx.close()
