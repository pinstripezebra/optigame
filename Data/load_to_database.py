from dotenv import load_dotenv
import pandas as pd
import psycopg2
import os

# Load environment variables from .env2 file
load_dotenv(dotenv_path=".env2")

df = pd.read_csv("Data/raw_data/total_results_with_description.csv")


conn = psycopg2.connect(os.environ.get("POST_DB_LINK"), sslmode='require')

def create_games_table():

    """ Connect to the PostgreSQL database and create games table
    if it doesnt exist."""

    # Create a cursor object
    cursor = conn.cursor()
    # Execute a query to create a table
    cursor.execute("""CREATE TABLE IF NOT EXISTS products (
        asin varchar(255),
        title varchar(255),
        price varchar(1000),
        rating varchar(255),
        rating_count varchar(255),
        description text,
        image_url varchar(255),
        product_url varchar(255)
    )""")

    conn.commit()
    # Close the cursor and connection
    cursor.close()
    conn.close()

def populate_games_table(df):

    """ Connect to the PostgreSQL database and populate games table
    with data from the dataframe."""

    # Create a cursor object
    cursor = conn.cursor()

    # Iterate over the rows of the DataFrame and insert each row into the table
    for index, row in df.iterrows():
        cursor.execute("""INSERT INTO products (asin, title, price, rating, rating_count, description, image_url, product_url)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                       (row['asin'], row['title'], row['price'], row['rating'], row['reviews_count'],
                        row['description'], row['image_url'], row['product_url']))

    conn.commit()
    # Close the cursor and connection
    cursor.close()
    conn.close()