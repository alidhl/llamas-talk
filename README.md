# Llamas Talk 🦙💬

Welcome to Llamas Talk, an engaging debate program where two chatbots argue over a chosen topic. This project provides a dynamic platform for chatbots to demonstrate their debating skills, utilizing both local and online chatbots as per user preference.

## Features

- **Chatbot Selection**: Choose between local models like Llama 3 or online models powered by OpenAI.
- **Customization**: Users can customize each debater's name, persona, and the topic of the debate.
- **Web Interface**: Built using Streamlit, the interface is clean and user-friendly.

## Demo

Check out the live demo here: [Llamas Talk Demo](https://llamas-talk.streamlit.app/)

*Note: The demo website is hosted on a CPU-only server, hence it only supports the online model. To use local models, you will need to run the Streamlit app locally.*

## Usage

This application offers flexible customization options for each debate session:

- **Selecting Chatbot Type**: Choose between local models, such as Llama 3, or online models powered by OpenAI to act as debaters.
- **Debate Topic**: Choose or input a specific topic for the debate.
- **Customizing Debaters**: For each chatbot, you can specify:
  - **Name**: Assign a unique name to each debater.
  - **Persona**: Create a distinct persona that the chatbot will embody during the debate.
- **Predefined Options**: There are predefined options, each associated with its own avatar. These can be selected to quickly configure the debaters with a set persona and visual representation.
- **Initiate the Debate**: Once the debaters are configured, start the debate and observe as they engage in a dynamic exchange over the selected topic in real-time.

By configuring each debater’s attributes, users can enjoy a more tailored and engaging debating experience. Whether you opt for predefined settings or create a custom setup, Llamas Talk offers an immersive platform for showcasing chatbot rhetoric skills.
  
## Installation

To set up Llamas Talk on your local machine, follow these steps:
1. **Clone the repository:** 
2. **Install dependencies:**
```bash
pip install -r requirements.txt
```
3. **Run the Streamlit application:**
```bash
streamlit run app.py
```
## Video Using LLama 3
The topic was "Dark Souls 3 is better than Bloodborne"

https://github.com/alidhl/llamas-talk/assets/119793124/f586f482-2d10-454f-80a1-4106c17225a3


## Acknowledgments

- [Langchain](https://langchain.com/) for online chatbot services.
- [ollama](https://ollama.llamas.dev/) for local model support.
- [Streamlit](https://streamlit.io/) for hosting and web interface design.
