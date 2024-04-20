from tools.debate import Debate
import os
from uuid import uuid4

unique_id = uuid4().hex[0:8]
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "llamas-talk"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"

# Topic for the debate
topic = "Is Mario better than Luigi?"
# First debater:
a_name = "Mario Fan"
a_persona = "You are a Mario Fanboy. You believe that Mario is the best character in the Mario series."
# Second debater:
b_name ="Luige Fan"
b_persona = "You are a Luige Fanboy. You believe that Luige is the best character in the Mario series."

debate = Debate(topic=topic)
# Debater that uses ollama and llama3 model
debate.add_debater(persona=a_persona, name=a_name, use_ollama_chatbot=True, model_name="llama3")
# Debater that uses OpenAI model
debate.add_debater(persona=b_persona, name=b_name, use_ollama_chatbot=False)
debate.simulate_debate(5)