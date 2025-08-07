import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the HTML content of the news website
url = "https://www.bbc.com/news"
response = requests.get(url)

# Step 2: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find all headline tags (e.g., <h3> used by BBC for headlines)
headlines = soup.find_all("h3",class_="gs-c-promo-heading__title")
if not headlines:
   promo_anchors=soup.select("a.gs-c-promo-heading")
   headlines=[a for a in promo_anchors if a.text.strip()]
if not headlines:
   headlines=[a for a in soup.find_all("a",href=True) if "/news/" in a["href"] and a.text.strip()] 
# Step 4: Extract text from each headline and store in a list
headline_texts = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]
if not headlines:
   print("Np headlines found using known selectors.")
   
else:
    
   with open("headlines.txt", "w", encoding="utf-8") as file:
       for i, title in enumerate(headline_texts, start=1):
           file.write(f"{i}. {title}\n")
       print("✅ Headlines saved to headlines.txt")
