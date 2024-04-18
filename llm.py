import ollama
from rich import print as rprint

class LLM():
    def __init__(self, model_name, objective, persona_name):
        self.model_name = model_name
        self.persona_name = persona_name
        self.instructions = f"""
        Your name is {persona_name} and you will be having a debate with a another person to discuss about the following: {objective}.
You will be given a set of messages to respond to. Keep your responses short"""
        self.messages = ""

    def respond(self, message):
        self.messages += f"Opponent: {message}\n"
        prompt = f"{self.instructions}\n\n{self.messages}\n\nBased on the pervious messages what is your response?".strip()
        #rprint("[green]" + prompt)
        response = ollama.generate(model=self.model_name, prompt=prompt)['response']
        self.messages += f"You: {response}\n"
        return response
    

if __name__ == "__main__":
    model_name = "llama2"
    objective = "Climate Change"
    persona_name1 = "ClimateChangeLover"
    persona_name2 = "ClimateChangeHater"
    llm1 = LLM(model_name, objective, persona_name1)
    llm2 = LLM(model_name, objective, persona_name2)

    for _ in range(2):
        try:
            response = llm1.respond(response)
            rprint("[blue]" + response + '\n')
        except NameError:
            response = llm1.respond("")
            rprint("[blue]" + response + '\n')
        
        response = llm2.respond(response)
        rprint("[red]" + response + '\n')
        