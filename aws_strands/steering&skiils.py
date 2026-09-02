# //steering
# //for a complex agent front loading the all the instructions ,bussiness rules into a single prompt runs into a prompting wall ,which may lead the agent to ignore the instructions,hallucinate behaviors,or fail to follow critical procedures

# steering uses a modular prompting,instead of front loading all the instructions,you define context aware steering handlers that provide feedback at right movmement,each handler defines the bussiness rules to enforce and lifecycle hooks where agent should be validated,like before a tool call or returning a output
#  Skills suggest the right steps; steering enforces them.


# a skill is a skill.md file with frontmatter(name,description) and a procedure in the body,the agent reads the descriptions,then loads the full skill only when its relevant this is progressive disclosure
# e workshop ships three skills in the skills/ folder:

# refund-processing - how to handle refund requests
# order-tracking - how to check order status
# account-troubleshooting - how to handle account issues

load the skills using AgentSkills plugin
skills_plugin=AgentSkills(skills=["./skills"])
agent = Agent(
    tools=[lookup_customer, get_order_history, process_refund],
    plugins=[skills_plugin],//embeded the plugin here
    system_prompt="You are a customer service agent. Activate the appropriate "
                  "skill for step-by-step guidance.",
)

