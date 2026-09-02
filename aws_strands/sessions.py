# add file based persistence to the customer service agent .session mangement is all about the agent should continue from the previous conversation,a new agent with same session_id picks up where the last one left off
# an agent backed by the filesession manager that saves conversation history to disk and reloads it on restart
# if it is production it saves to cloud storage like amason s3 rather than local disk
# session manager persists the state seperately from the agent,filesession manager writes local JSON files ,reacreate the agent with the same session_id and the prior conversation is restored
agent = Agent(
    tools=[lookup_customer, get_order_history, process_refund],
    system_prompt="You are a customer service agent. Use prior context if available.",
)
agent("Hi, I'm customer C-1001. Can you look up my account?")

# Simulate a restart - a brand new instance
agent2 = Agent(
    tools=[lookup_customer, get_order_history, process_refund],
    system_prompt="You are a customer service agent. Use prior context if available.",
)
agent2("What was my account status again?")  # agent2 has no memory of C-1001