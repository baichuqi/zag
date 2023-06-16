import mysql.connector

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
        query = f'SELECT count(*) FROM {table_name}'
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        # Close the cursor and connection
        self.cursor.close()
        self.cnx.close()
