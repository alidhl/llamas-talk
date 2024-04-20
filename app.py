"""
Streamlit app for running a web interface debate between two chatbots. 
use main.py to run the debate locally or use the Streamlit app to run the debate in the browser by running streamlit run app.py in the terminal.
Demo uses cpu so only the online model is used.
Demo link: https://share.streamlit.io/llamas-ai/langchain/main/app.py
"""
import streamlit as st
from streamlit import components
from tools.debate import Debate

# Predefined options for each parameter
topics = ['Dark Souls 3 is better than Bloodborne', 'Custom']
names = ['Gwyn', 'Gehrman', 'Custom']
personas = ['A persona that likes Dark Souls 3', 'A persona that likes Bloodborne', 'Custom']
models = ['llama3', 'llama2', 'Custom (has to be downloaded on the system and compatible with Ollama)']

# User input for debate arguments
topic = st.selectbox('Select or enter the debate topic:', topics)
if topic == 'Custom':
    topic = st.text_input('Enter the debate topic:')

a_name = st.selectbox('Select or enter the name of the first debater:', names)
if a_name == 'Custom':
    a_name = st.text_input('Enter the name of the first debater:')

a_persona = st.selectbox('Select or enter the persona of the first debater:', personas)
if a_persona == 'Custom':
    a_persona = st.text_input('Enter the persona of the first debater:')

a_use_ollama = st.checkbox('Use Ollama for the first debater?')
a_model = st.selectbox('Select or enter the model for the first debater:', models) if a_use_ollama else None

b_name = st.selectbox('Select or enter the name of the second debater:', names)
if b_name == 'Custom':
    b_name = st.text_input('Enter the name of the second debater:')

b_persona = st.selectbox('Select or enter the persona of the second debater:', personas)
if b_persona == 'Custom':
    b_persona = st.text_input('Enter the persona of the second debater:')

b_use_ollama = st.checkbox('Use Ollama for the second debater?')
b_model = st.selectbox('Select or enter the model for the second debater:', models) if b_use_ollama else None

# Create placeholders for the chat
chat_placeholder = st.empty()

if st.button('Start Debate'):
    # Clear the page
    st.write('\n' * 100)

    # Create Debate instance
    debate = Debate(topic=topic)

    # Add debaters
    debate.add_debater(name=a_name, persona=a_persona, use_ollama_chatbot=a_use_ollama, model_name=a_model)
    debate.add_debater(name=b_name, persona=b_persona, use_ollama_chatbot=b_use_ollama, model_name=b_model)

    # Create placeholders for chat messages
    placeholders = [st.empty() for _ in range(5)]

    # Simulate debate and display result
    for i, response in enumerate(debate.simulate_debate_generator(5)):
        # Update the placeholder with the new message
        placeholders[i].text(response)