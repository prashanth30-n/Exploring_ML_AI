from strands import Agent
from strands.session.file_session_manager import FileSessionManager

##to use store the previous conversations history for the agents for the context 

Session_manager=FileSessionManager(session_id="customer_suport",base_dir="'/agent_sessions")# file bases storage we can use aws s3 sevices to store the converstaion histories

agent=Agent(
    id="support_bot_1",
    session_manager=Session_manager,
    tools=[knowledge_base,ticket_system] ## not defined tools definition
)

agent("Help me reset my password") 
agent("I can't access my email") 


##later ,even after a restart ,restore the full conversation

restored_session_manager = FileSessionManager(session_id=”customer_support”, base_dir="./agent_sessions") 

restored_agent = Agent( 
    id="support_bot_1",  
    session_manager=restored_session_manager, 
    tools=[knowledge_base, ticket_system] 
) 
