from models.chatbot import Chatbot
from models.ollama_chatbot import OllamaChatbot
from rich import print

class Debate():
    def __init__(self, topic):
        """
        Initializes a Debate object.

        Args:
            topic (str): The topic of the debate.
        """
        self.debate_topic = topic
        self.debaters = []

    def add_debater(self, persona, name, use_ollama_chatbot=False, model_name=None):
        """
        Adds a debater to the debate.

        Args:
            persona (str): The persona of the chatbot.
            name (str): The name of the chatbot.
            use_ollama_chatbot (bool, optional): Whether to use the ollama chatbot (local models like llama3). Defaults to False.
            model_name (str, optional): The model name for the ollama. Required if use_ollama_chatbot is True. Needs to be compatible with ollama and downloaded on the system.
        """
        if len(self.debaters) >= 2:
            raise Exception("Cannot add more than two debaters.")
        
        if use_ollama_chatbot:
            if model_name is None:
                raise Exception("Model name is required for local chatbot.")
            chatbot = OllamaChatbot(persona, self.debate_topic, model_name)
        else:
            chatbot = Chatbot(persona, self.debate_topic)
        
        self.debaters.append((name, chatbot))

    def simulate_debate(self, num_turns=10):
        """
        Simulates a debate between two chatbots.

        Args:
            num_turns (int, optional): The number of turns in the debate. Defaults to 10.
        """
        if len(self.debaters) < 2:
            raise Exception("Cannot start a debate with less than two debaters.")
        
        message = "Let's start the debate."
        for _ in range(num_turns):
            for name, chatbot in self.debaters:
                message = chatbot.respond(message)
                print(f"[bold cyan]{name}:[/bold cyan]", message + "\n")

    def simulate_debate_generator(self, num_turns=10):
        """
        Simulates a debate between two chatbots and yields the responses one by one.

        Args:
            num_turns (int, optional): The number of turns in the debate. Defaults to 10.
        """
        message = "Let's start the debate."
        for _ in range(num_turns):
            for name, chatbot in self.debaters:
                message = chatbot.respond(message)
                yield f"{name}: {message}"