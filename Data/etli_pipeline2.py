from oxylabs import RealtimeClient
from dotenv import load_dotenv
import os
import json
from utils.amazon_api import convert_to_dataframe, add_description, parse_results
from utils.db_handler import DatabaseHandler

# Load environment variables from .env2 file
load_dotenv(dotenv_path=".env2")

# Set your Oxylabs API Credentials.
username = os.environ.get("USERNAME_OXY")
password = os.environ.get("PASSWORD_OXY")

# Initialize the Realtime client with your credentials.
client = RealtimeClient(username, password)

# searching for board games
result = client.amazon.scrape_search(query="board games", 
                                     country="us", 
                                     page=2, 
                                     max_results=30, 
                                     parse=True,
                                     context = [{'key': 'autoselect_variant', 'value': True}])

# parsing results
combined_df = parse_results(result)

# adding descriptions
combined_df = add_description(combined_df, username, password)
combined_df.to_csv("Data/raw_data/total_results_with_description.csv", index=False)

table_name = "optigame_products"
table_creation_query = """CREATE TABLE IF NOT EXISTS optigame_products (
    id UUID PRIMARY KEY,
    asin VARCHAR(255),
    title TEXT,
    price FLOAT,
    rating FLOAT,
    sales_volume TEXT,
    description TEXT,
    reviews_count INTEGER
        )
    """


# Deleting the table if it exists
delete_table(table_name)
# Create the table if it doesn't exist
create_table(table_creation_query)
# Populate the table with data from the DataFrame
populate_table(df)
# returning data from the database
df = retrieve_all_from_table(table_name)
print(df)
print("Data loaded successfully into the database.")