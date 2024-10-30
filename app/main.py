import os
import tempfile

import streamlit as st
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    #Streamlit is used to create an interactive user interface
    st.title("📧 Cold Mail Generator")
    cv_pdf = st.file_uploader(label='UPLOAD YOUR CV', type=['pdf'])
    url_input = st.text_input("Enter a URL: ")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader(url_input)
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            job = jobs[0]
            skills = job.get('skills', [])
            links = portfolio.query_links(skills)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(cv_pdf.read())
                tmp_file_path = tmp_file.name

            # Load and clean the uploaded CV
            pdf_loader = PyPDFLoader(tmp_file_path)
            cv_documents = pdf_loader.load()
            if not cv_documents:
                st.error("Failed to read the uploaded CV.")
                os.unlink(tmp_file_path)  # Clean up the temporary file
                return
            # Combine text from all pages of the PDF and clean it
            cv_text = clean_text(" ".join([doc.page_content for doc in cv_documents]))

            # Clean up the temporary file
            os.unlink(tmp_file_path)
            email = llm.write_mail(job, links, cv_text)
            st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)

