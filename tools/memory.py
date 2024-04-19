class Memory:
    def __init__(self , k):
        self.messages = []
        self.k = k # This indicate to the chat turns window
        self.formatted_messages = ''

    def add_message(self, sender, text:str):
        self.messages.append({"sender": sender, "text": text})
        self.formatted_messages = self.formatted_messages + sender + ": " + text +"\n"
        return text.strip()

    def get_messages(self):
        return self.messages

    def format_messages(self):
        """
        This function will return the last k characters of the chat and format it so the llm can understand it 

        Args:
        k :int -> this means the number of characters you want the llm remember bigger means longer memory
        Return:
        formatted_messages :str -> it will return the chat history as a string
        """
        num_characters = min(len(self.formatted_messages) , self.k)

        return self.formatted_messages[-num_characters:]
