import ollama
from rich import print as rprint
from memory import Memory

class LLM():
    def __init__(self, model_name, objective, persona_name):
        self.model_name = model_name
        self.persona_name = persona_name
        self.objective = objective
        self.chat_history = Memory(100)

    def generate_prompt(self):
        return self.chat_history.format_messages()

    def respond(self, message):
        self.chat_history.add_message("Opponent", message)
        prompt = self.generate_prompt()
        response = ollama.generate(model=self.model_name, prompt=prompt)['response']
        self.chat_history.add_message("You:", response)
        return response
    

if __name__ == "__main__":
    model_name = "llama3"
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