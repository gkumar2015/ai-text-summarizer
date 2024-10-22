# import all the relevant libraries
import streamlit as st
from langchain_openai import OpenAI
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

# function to interact with OpenAI and return response
def generate_response(user_input_txt):
    # Instantiate the LLM model
    llm = OpenAI(temperature=0.5, openai_api_key=openai_api_key)
    # Split the text
    text_splitter = CharacterTextSplitter()
    txt_split = text_splitter.split_text(user_input_txt)
    # Create multiple documents
    docs = [Document(page_content=t) for t in txt_split]
    # Text summarization
    chain = load_summarize_chain(llm, chain_type='map_reduce')
    return chain.invoke(docs)

# Page title
st.title('🦜🔗 👑 AI Text Summarizer')

# Text input
txt_user_input = st.text_area('Enter your input text- 🧑‍🎓', '', height=350)

# Form to accept user's text input for summarization
result = []
with st.form('summarize_form', clear_on_submit=True):
    
    openai_api_key = st.sidebar.text_input('OpenAI API Key', type = 'password')
    submitted = st.form_submit_button('Submit- Summarize Text')
    
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted and openai_api_key.startswith('sk-'):
        with st.spinner('Please wait- summarizing text...'):
            response = generate_response(txt_user_input)
            result.append(response)
            del openai_api_key

if len(result):
    st.info(response["output_text"])
