from langchain_community.llms.ollama import Ollama
from langchain.memory import ChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
class llm():
    def __init__(self, model_name, subject):
        model = Ollama(model=model_name, num_predict= 64)
        self.history = ChatMessageHistory()
        prompt = f"You are chatting with another llm about {subject} make sure to stick to the topic."
        prompt_template = ChatPromptTemplate.from_messages([
            ('system', prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])
        self.chain = prompt_template | model | StrOutputParser()
    def respond(self, message):
        self.history.add_user_message(message)
        print(self.history.messages)
        response = self.chain.invoke({"messages" : self.history.messages})
        self.history.add_ai_message(response)
        return response
    def start_conversation(self):
        response = self.chain.invoke({"messages" : self.history.messages})
        return response

if __name__ == "__main__":
    ai1 = llm('llama2', "Computer Science")
    ai2 = llm('llama2', "Computer Science")
    r1 = ai1.start_conversation()
    print("AI1: ", r1)
    for i in range(3):
        r2 = ai2.respond(r1)
        print('AI2: ', r2)
        r1 = ai1.respond(r2)
        print('AI1: ', r1)