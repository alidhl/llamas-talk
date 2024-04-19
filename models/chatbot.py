from tools.prompts import DEBATE_PROMPT
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from tools.memory import Memory
from operator import itemgetter
class Chatbot:
    def __init__(self, persona, objective):
        chat = ChatOpenAI()
        system_prompt = DEBATE_PROMPT
        self.objective = objective
        self.persona = persona
        self.chat_history = Memory(1000)
        prompt = ChatPromptTemplate.from_template(system_prompt)
        context = RunnableParallel({
            "objective" :  itemgetter('objective')| RunnablePassthrough(),
            "persona" : itemgetter('persona')| RunnablePassthrough(),
            "chat_history" : itemgetter('chat_history')| RunnablePassthrough(),
        })
        self.chain = context | prompt | chat | StrOutputParser()
    
    def respond(self, message):
        self.chat_history.add_message("Opponent", message)
        res = self.chain.invoke({"objective": self.objective, "persona": self.persona, "chat_history" : self.chat_history.format_messages()})
        self.chat_history.add_message("You", res)
        return res
    