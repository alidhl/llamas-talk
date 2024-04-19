from debate import Debate

# Topic for the debate
topic = "Is Mario better than Luigi?"
# First debater:
a_name = "Mario Fan"
a_persona = "You are a Mario Fanboy. You believe that Mario is the best character in the Mario series."
# Second debater:
b_name ="Luige Fan"
b_persona = "You are a Luige Fanboy. You believe that Luige is the best character in the Mario series."

debate = Debate(persona1= a_persona, persona2= b_persona, topic=topic, name1=a_name, name2=b_name)
debate.simulate_debate(5)