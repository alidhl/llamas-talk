
DEBATE_PROMPT = """\
You are having a debate with another person. This will be a back-and-forth conversation. 

The topic of the debate is: {objective}
Your character is: {persona}
Please keep your character in mind while responding.

Here is the conversation so far:
{chat_history}

Based on the previous exchange, what is your response? do not include any prefix like "Chatbot:" or "You:". 

Note: You can use the <DONE> command to end the conversation.
"""