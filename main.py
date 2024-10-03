import streamlit as st
from scrape import scrape, split_content, clean_body_content, body_content

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")


if st.button("Scrap Data"):
    st.write("Scrap Website ...")
    result = scrape(url)
    body_content = body_content(result)
    clean_content = clean_body_content(body_content)

    st.session_state.dom_content = clean_content

    with st.expander("View Dom Content"):
        st.text_area("Dom Content", clean_content, height=300)

    if "dom_content" in st.session_state:
        parse_description = st.text_area("Describe what you want to parse: ")

        if st.button('Parse Content'):
            if parse_description:
                st.write('Parsing the content')

                dom_chunks = split_content(st.session_state.dom_content)
