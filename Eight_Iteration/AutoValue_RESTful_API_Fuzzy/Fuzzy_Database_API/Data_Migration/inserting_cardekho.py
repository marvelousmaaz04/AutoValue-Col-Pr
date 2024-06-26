import psycopg2

import csv
import psycopg2
from psycopg2 import sql

# Function to connect to PostgreSQL
def connect():
    try:
        conn = psycopg2.connect(
            dbname="cardekho_car_listings",
            user="postgres",
            password="server",
            host="localhost",
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e)
        return None

# Function to insert data into PostgreSQL table from CSV
def insert_data_from_csv(conn, table_name, csv_file_path):
    try:
        cursor = conn.cursor()
        with open(csv_file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row if it exists
            for row in reader:
                # Assuming CSV columns match table columns in the same order
                insert_query = sql.SQL("INSERT INTO {} VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s)").format(sql.Identifier(table_name))
                cursor.execute(insert_query, row)
        conn.commit()
        print("Data inserted successfully")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting data into PostgreSQL")
        print(e)

# Main function
def main():
    conn = connect()
    if conn is not None:
        table_name = "cardekho_pune"
        csv_file_path = "cardekho_csvs/cardekho_pune.csv"
        insert_data_from_csv(conn, table_name, csv_file_path)
        conn.close()

if __name__ == "__main__":
    main()
