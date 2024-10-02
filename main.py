import streamlit as st
from scrape import scrape

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")


if st.button("Scrap Data"):
    st.write("Web scrapping complete")
    result = scrape(url)
    print(result)
