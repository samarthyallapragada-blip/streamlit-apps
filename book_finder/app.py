import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("📚 Book Finder")
st.caption("Scraping books from books.toscrape.com")

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

for book in books[:10]:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]
    st.metric(label=title, value=price)
    st.caption(f"Rating: {rating.capitalize()}")
    st.divider()
