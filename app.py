import streamlit as st
from tools.debate import Debate
import os
# App title
st.set_page_config(page_title="🦙💬 LLamas Talk")

st.title("🦙💬 LLamas Talk")
st.write('A Debate between two chatbots using either Ollama or OpenAI API.')
# Define avatar URLs for predefined names
avatars = {
    'Gwyn': 'https://i.ytimg.com/vi/G4K0qjpuJwc/maxresdefault.jpg',
    'Gehrman': 'https://bloodborne.wiki.fextralife.com/file/Bloodborne/Gehrman%20Close-up.jpg',
    'Mario': 'https://tiermaker.com/images/templates/1061544140967.png',
    'Luigi': 'https://static1.personality-database.com/profile_images/566721b959f24a8ab3ab76cc0833f670.png',
}

with st.sidebar:
    # Predefined options for each parameter
    topics = ['Is Mario better than Luigi?', 'Dark Souls 3 is better than Bloodborne', 'Custom']
    names = ['Mario', 'Luigi', 'Gwyn', 'Gehrman', 'Custom']
    personas = [
    'You are an avid fan of Mario. You believe that Mario, with his iconic red hat and blue overalls, is the best character in the Mario series due to his balanced abilities and his role as the protagonist in most games.',
    'You are a dedicated supporter of Luigi. You argue that Luigi, often overshadowed by his brother Mario, is actually the superior character in the Mario series because of his unique abilities, like his higher jump, and his starring role in the Luigi\'s Mansion series.',
    'You are a passionate player of Dark Souls 3. You appreciate its challenging gameplay, intricate world design, and deep lore, and you believe it\'s one of the best action RPGs ever made.',
    'You are a fervent admirer of Bloodborne. You argue that Bloodborne\'s faster-paced combat, gothic horror setting, and complex narrative make it a standout title in the action RPG genre.',
    'Custom'
    ]
    models = ['llama3', 'llama2', 'Custom (has to be downloaded on the system and compatible with Ollama)']

    st.sidebar.title("Debate Settings")
    st.write("Please enter your OpenAI API key to use OpenAI models. Only necessary if you won't use Ollama.")
    openai_api_key = st.sidebar.text_input("OpenAI API Key", key= "chatbot_api_key" , type="password")
    # User input for debate arguments
    topic = st.selectbox('Select or enter the debate topic:', topics, index=0)
    if topic == 'Custom':
        topic = st.text_input('Enter the debate topic:')

    a_name = st.selectbox('Select or enter the name of the first debater:', names, index=0)
    if a_name == 'Custom':
        a_name = st.text_input('Enter the name of the first debater:')

    a_persona = st.selectbox('Select or enter the persona of the first debater:', personas, index=0)
    if a_persona == 'Custom':
        a_persona = st.text_input('Enter the persona of the first debater:')

    b_name = st.selectbox('Select or enter the name of the second debater:', names, index=1)
    if b_name == 'Custom':
        b_name = st.text_input('Enter the name of the second debater:')

    b_persona = st.selectbox('Select or enter the persona of the second debater:', personas, index=1)
    if b_persona == 'Custom':
        b_persona = st.text_input('Enter the persona of the second debater:')

    st.write('You can use Ollama to use local models like llama3. However, this is for local use only won\'t work on the deployed app.')
    a_use_ollama = st.checkbox('Use Ollama for the first debater?')
    a_model = st.selectbox('Select or enter the model for the first debater:', models) if a_use_ollama else None

    b_use_ollama = st.checkbox('Use Ollama for the second debater?')
    b_model = st.selectbox('Select or enter the model for the second debater:', models) if b_use_ollama else None

    num_turns = st.sidebar.number_input('Enter the number of turns for the debate:', min_value=1, value=2)

    # Clear chat history button
    def clear_chat_history():
        st.session_state.messages = []
    st.button('Clear Chat History', on_click=clear_chat_history)


if "messages" not in st.session_state.keys():
    st.session_state.messages = []
    
# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Try to get the OpenAI API key from the environment variables usefull if run locally
openai_api_key = os.getenv('OPENAI_API_KEY')

if st.button('Start Debate'):
    # If one of the debaters is using OpenAI API, check if the API key is provided
    if not a_use_ollama or not b_use_ollama:
        if not openai_api_key:
            st.info("Please add your OpenAI API to continue.")
            st.stop()
        os.environ['OPENAI_API_KEY'] = openai_api_key
    # Create Debate instance
    debate = Debate(topic=topic)
    # Add debaters
    debate.add_debater(name=a_name, persona=a_persona, use_ollama_chatbot=a_use_ollama, model_name=a_model)
    debate.add_debater(name=b_name, persona=b_persona, use_ollama_chatbot=b_use_ollama, model_name=b_model)
    # Simulate debate and display result
    for response , name in debate.simulate_debate_generator(num_turns=num_turns):
        st.session_state.messages.append({"role": f"{name}", "content": response})
        with st.chat_message(f"{name}", avatar=avatars[name] if name in avatars else None):#avatars[name] if name in avatars else None
            
            st.write(f"**{name}**: " + response)
            
    st.markdown("## **The Debate has finished.**")