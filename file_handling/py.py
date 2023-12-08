import mysql.connector

# Configuration for the MySQL connection
config = {
    'user': 'root',
    'password': 'Sumedh@123',
    'host': '127.0.0.1',
    'database': 'isourse',
    'raise_on_warnings': True
}

try:
    # Establish a connection to the MySQL server
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print('Connected to MySQL database')

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    # Close the connection in the finally block
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print('MySQL connection closed')
