import requests
from bs4 import BeautifulSoup
import pandas as pd

# Dictionary to store the data
data = {"title": [], "price": []}

# URL of the website to scrape
url = "https://outfitters.com.pk/collections/men-t-shirts-and-polos"

# Headers to mimic a request from a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

# Make a GET request to fetch the raw HTML content
r = requests.get(url, headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

# Select all product elements (assumes product titles are within a tags with class 'product-link-main')
product_titles = soup.select("a.product-link-main")

# Select all price elements (assumes prices are within span tags with class 'money')
product_prices = soup.select("span.money")

# Loop through the product titles and append to the data dictionary
for title in product_titles:
    data["title"].append(title.get_text(strip=True))

# Loop through the product prices and append to the data dictionary
for price in product_prices:
    data["price"].append(price.get_text(strip=True))

# Check the lengths of the lists
titles_length = len(data["title"])
prices_length = len(data["price"])

print(f"Titles: {titles_length}, Prices: {prices_length}")

# Ensure the lengths of both lists are the same
min_length = min(titles_length, prices_length)
data["title"] = data["title"][:min_length]
data["price"] = data["price"][:min_length]

# Print the collected data
print(data)

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv", index=False)

print("Data saved to data.csv")

