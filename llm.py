import ollama
from rich import print as rprint

class LLM():
    def __init__(self, model_name, objective, persona_name):
        self.model_name = model_name
        self.persona_name = persona_name
        self.instructions = f"""
You are a {persona_name} and you will be having a debate with a another person to discuss about the following: {objective}. Try to reach an agreement
You will be given last exchange of messages. Keep your responses short"""
        self.last_opponent_message = ""
        self.last_response = ""

    def generate_prompt(self):
        if not self.last_opponent_message:  # If it's the first message
            return f"{self.instructions}\n\n{self.last_opponent_message}\n\nThis is the start of the conversation. What is your response?"
        else:
            return f"{self.instructions}\n\n{self.last_opponent_message}\n\n{self.last_response}\n\nBased on the previous Exchange what is your response? If you think you have reached an agreement with your opponent, respond with <DONE> only if you have nothing to add and do not add any other information.".strip()

    def respond(self, message):
        self.last_opponent_message = f"Opponent: {message}"
        prompt = self.generate_prompt()
        #rprint("[green]" + prompt)
        response = ollama.generate(model=self.model_name, prompt=prompt)['response']
        self.last_response = f"You: {response}"
        return response
    

if __name__ == "__main__":
    model_name = "llama2"
    objective = "Mario is better than Luigi."
    persona_name1 = "Mario Fanboy"
    persona_name2 = "Luigi Fanboy"
    llm1 = LLM(model_name, objective, persona_name1)
    llm2 = LLM(model_name, objective, persona_name2)

    response1 = ""
    response2 = ""
    for _ in range(15):
        response1 = llm1.respond(response2)
        rprint("[blue]" + response1 + '\n')

        response2 = llm2.respond(response1)
        rprint("[red]" + response2 + '\n')

        if "<DONE>" in response1 and "<DONE>" in response2:
            break
        