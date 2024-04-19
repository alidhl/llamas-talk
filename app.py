import streamlit as st
from tools.debate import Debate

# User input for debate arguments
topic = st.text_input('Enter the debate topic:')
a_name = st.text_input('Enter the name of the first debater:')
a_persona = st.text_input('Enter the persona of the first debater:')
b_name = st.text_input('Enter the name of the second debater:')
b_persona = st.text_input('Enter the persona of the second debater:')
use_local_chatbot = st.checkbox('Use local chatbot?')

if st.button('Start Debate'):
    # Create Debate instance with user input
    debate = Debate(persona1=a_persona, persona2=b_persona, topic=topic, name1=a_name, name2=b_name, use_local_chatbot=use_local_chatbot)
    
    # Simulate debate and display result
    for response in debate.simulate_debate_generator(5):
        st.write(response)