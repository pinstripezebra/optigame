from oxylabs import RealtimeClient

# Set your Oxylabs API Credentials.
username = "username"
password = "password"

# Initialize the Realtime client with your credentials.
client = RealtimeClient(username, password)

# Use `bing_search` as a source to scrape Bing with nike as a query.
result = client.bing.scrape_search("nike")

print(result.raw)