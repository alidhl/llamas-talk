import ollama
from tools.memory import Memory
from tools.prompts import DEBATE_PROMPT

class LocalChatbot():
    def __init__(self, persona, objective, model_name="llama3"):
        self.model_name = model_name
        self.persona = persona
        self.objective = objective
        self.chat_history = Memory(1000)
        self.prompt = DEBATE_PROMPT
    
    def generate_prompt(self):
        chat_history = self.chat_history.format_messages()
        self.prompt = DEBATE_PROMPT.format(objective=self.objective, persona=self.persona, chat_history=chat_history)

    def respond(self, message):
        self.chat_history.add_message("Opponent", message)
        self.generate_prompt()
        response = ollama.generate(model=self.model_name, prompt=self.prompt)['response']
        self.chat_history.add_message("You", response)
        return response
    
