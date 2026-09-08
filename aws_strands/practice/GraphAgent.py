# 

from strands import Agent
from strands.multiagent import GraphBuilder

analyser_agent=Agent(
    name='analyser',
    system_prompt="Analyze customer requests and categorize them",
    tools=[text_classifier, sentiment_analyzer]
)
normal_processor=Agent(
    name="normal_processor",
    system_prompt="handle routine requests automaticaaly",
    tools=[knowledge_base,auto_responder]
)
critical_processor=Agent(
    name="critical_processor",
    system_prompt="handle critical requests quickly",
    tools=[knowledge_base, escalate_to_support_agent]  
)

builder=GraphBuilder()
builder.add_node(analyser_agent,"analyse")
builder.add_node(normal_processor,"normal_processor")
builder.add_node(critical_processor,"critical_processor")

def is_approved(state): 
    return True 

def is_critical(state): 
    return False 

builder.add_edge("analyse","normal_processor",condition=is_approved)
builder.add_edge("analyse","critical_processor",condition=is_critical)
builder.set_entry_point("analyse")
customer_support_graph=builder.build()

results=customer_support_graph("I need help with my order")