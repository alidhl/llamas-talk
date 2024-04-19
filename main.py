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
# Use the local chatbot via ollama (llama3) or the OpenAI chatbot
use_local_chatbot = True

debate = Debate(persona1= a_persona, persona2= b_persona, topic=topic, name1=a_name, name2=b_name, use_local_chatbot=use_local_chatbot)
debate.simulate_debate(5)