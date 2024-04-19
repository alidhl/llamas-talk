from models.chatbot import Chatbot
from models.local_chatbot import LocalChatbot
from rich import print

class Debate():
    def __init__(self, persona1, persona2, topic, name1="Chatbot 1", name2="Chatbot 2", use_local_chatbot=False):
        """
        Initializes a Debate object.

        Args:
            persona1 (str): The persona of chatbot 1.
            persona2 (str): The persona of chatbot 2.
            topic (str): The topic of the debate.
            name1 (str, optional): The name of chatbot 1. Defaults to "Chatbot 1".
            name2 (str, optional): The name of chatbot 2. Defaults to "Chatbot 2".
            use_local_chatbot (bool, optional): Whether to use the local chatbot (llama3). Defaults to False.
        """
        if use_local_chatbot:
            self.chatbot1 = LocalChatbot(persona1, topic)
            self.chatbot2 = LocalChatbot(persona2, topic)
        else:
            self.chatbot1 = Chatbot(persona1, topic)
            self.chatbot2 = Chatbot(persona2, topic)
        self.name1 = name1
        self.name2 = name2
    
    def simulate_debate(self, num_turns=10):
        """
        Simulates a debate between two chatbots.

        Args:
            num_turns (int, optional): The number of turns in the debate. Defaults to 10.
        """
        message = "Let's start the debate."
        for _ in range(num_turns):
            message = self.chatbot1.respond(message)
            print(f"[bold cyan]{self.name1}:[/bold cyan]", message + "\n")
            message = self.chatbot2.respond(message)
            print(f"[bold magenta]{self.name2}:[/bold magenta]", message + "\n")
            
    def simulate_debate_generator(self, num_turns=10):
        """
        Simulates a debate between two chatbots and yields the responses one by one.

        Args:
            num_turns (int, optional): The number of turns in the debate. Defaults to 10.
        """
        message = "Let's start the debate."
        for _ in range(num_turns):
            message = self.chatbot1.respond(message)
            yield f"{self.name1}: {message}"
            message = self.chatbot2.respond(message)
            yield f"{self.name2}: {message}"