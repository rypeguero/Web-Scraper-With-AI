import streamlit as st
from Scrape import (scrape_website, extract_body_content,
clean_body_content,split_dom_content)
from parse import parse_with_ollama

#UI Streamlit
st.title("Web Scraper With AI")
url = st.text_input("Enter the Website URL: ")

#Website Scraper
if st.button("Scrape Site"):
    if url:
        st.write("Scraping The Website")

        #Scraping the website
        dom_content = scrape_website(url)
        body_content = extract_body_content(dom_content)
        cleaned_content = clean_body_content(body_content)

        #Storing the DOM content in Streamlit session state
        st.session_state.dom_content = cleaned_content

        #Displaying DOM content in a text box
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content,height=350)

#Asking questions about the DOM content
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse"):
        if parse_description:
            st.write("Parsing The Content. . .")

            #parsing the content with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)


    result = scrape_website(url)
    print(result)
