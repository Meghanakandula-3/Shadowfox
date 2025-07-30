import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "https://quotes.toscrape.com/"

# Send request
response = requests.get(url)

# Parse with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all quotes
quotes = soup.find_all("div", class_="quote")

# Prepare CSV
with open("quotes.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])

    # Loop through each quote block
    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]
        writer.writerow([text, author, ", ".join(tags)])

print(" Quotes saved to quotes.csv")