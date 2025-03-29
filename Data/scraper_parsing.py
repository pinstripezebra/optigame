import json


def parse_item(item):
    # Extract the relevant fields from the item
    return {
        "asin": item["asin"],
        "title": item["title"],
        "price": item["price"],
        "rating": item["rating"],
        "sales_volume": item["sales_volume"],
        "reviews_count": item["reviews_count"]}

# Read the JSON object from the .txt file
with open("Data/output.txt", "r", encoding="utf-8") as file:
    data_paid = json.load(file)['results'][0]['content']['results']['paid']  # paid results
    #data_organic = json.load(file)['results'][0]['content']['results']['organic'] # organic results


# Print the list
print([parse_item(i) for i in data_paid])
#print(len(data_organic))