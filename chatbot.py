from prompts import DEBATE_PROMPT
from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from memory import Memory

class Chatbot:
    def __init__(self, persona, objective, model_name='llama3'):
        chat = ChatOpenAI()
        system_prompt = DEBATE_PROMPT
        self.objective = objective
        self.persona = persona
        self.chat_history = Memory(1000)
        prompt = ChatPromptTemplate.from_template(system_prompt)
        context = RunnableParallel({
            "objective" : RunnablePassthrough(),
            "persona" : RunnablePassthrough(),
            "chat_history" : RunnablePassthrough(),
        })
        self.chain = context | prompt | chat | StrOutputParser()
    
    def respond(self, message):
        self.chat_history.add_message("Opponent", message)
        res = self.chain.invoke({"objective": self.objective, "persona": self.persona, "chat_history" : self.chat_history.format_messages()})
        self.chat_history.add_message("You:", res)
        return res
    
    
if __name__ == "__main__":
    persona = "You are a Mario Fanboy. You believe that Mario is the best character in the Mario series."
    objective = "Is Mario better than Luigi?"
    chatbot = Chatbot(persona, objective)
    
    response = chatbot.respond("Come on man of course luige is better how is this a debate")
    print(response)