import ollama
import rich
class LLM():
    def __init__(self, model_name, objective, persona_name):
        self.model_name = model_name
        self.persona_name = persona_name
        instructions = f"Your name is {persona_name} and you will be chatting with a another person to discuss about the following: {objective}. You will be given a set of messages to respond to. Keep your responses short"
        self.messages = ""
        self.prompt =f"""{instructions}\n\n{self.messages}"""

    def respond(self, message):
        self.messages += f"User: {message}\n"
        self.prompt = f"{self.prompt}\n{self.messages}"
        print
        response = ollama.generate(model=self.model_name, prompt=self.prompt)
        self.messages += f"{self.persona_name}: {response}\n"
        self.prompt = f"{self.prompt}\n{self.messages}"
        return response
    

if __name__ == "__main__":
    model_name = "llama2"
    objective = "the importance of climate change"
    persona_name1 = "ClimateChangeLover"
    persona_name2 = "ClimateChangeHater"
    llm1 = LLM(model_name, objective, persona_name1)
    llm2 = LLM(model_name, objective, persona_name2)
    message = "What are your thoughts on climate change?"

    for _ in range(3):
        response1 = llm1.respond(message)
        print(f"{llm1.persona_name}: {response1['response']}")
        print("-"*50)
        message = response1
        response2 = llm2.respond(message)
        print(f"{llm2.persona_name}: {response2['response']}")

        message = response2