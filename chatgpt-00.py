import openai
import streamlit as st

import os
import dotenv
dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_API_ENDPOINT = os.getenv('OPENAI_API_ENDPOINT')
OPENAI_API_TYPE = 'azure'
OPENAI_API_VERSION = '2023-05-15'

openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = OPENAI_API_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = OPENAI_API_VERSION

st.header("AI Poem Generator", divider="rainbow")

name = st.text_input("Input Name : ")
if name:
    st.write(f"Hello {name}! How can I help you today?")

subject = st.text_input("Input Subject : ")
content = st.text_input("Input Content : ")

button_result = st.button("Run")
if button_result:
    with st.spinner("Generating poem..."):
        result = openai.chat.completions.create(
            model="dev-gpt-35-turbo",
            messages=[
                {"role" : "system", "content" : "you are a poem generator."},
                {"role" : "user", "content" : "Name of the writer is " + name},
                {"role" : "user", "content" : "Subject of poem is " + subject},
                {"role" : "user", "content" : "Content of poem is " + content},
                {"role" : "user", "content" : "Based on the above information, please generate a poem."}
            ]
        )
    
    st.write(result.choices[0].message.content)
    st.success("Poem generated successfully!")