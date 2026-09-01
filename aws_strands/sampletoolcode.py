from strands import tool
//this is a random tool for an agent which looks up customers,check orders and processes refunds 
//the @tool is called as docstring and the tool returns a string which becomes the tool result fed back into the agent loop
@tool //making our function as tool by mentioning this tag meaning the agent can recoginse this//
//generally we define the tools in a sepearate .py extenstion file 
//now we define the loop and agent in chat.py which is sepearte with tools the code will have a loop while(true) until user clicks exit
def lookup_customer(customer_id:str)->str:
    """
    Look up a customer by their ID //this line tells what tool does 
    
    Args:
    customer_id:The customer ID(e.g c-1001) //this line documents the parameters required for the tool not only for the humans but also for the humans
    """
    customer=CUSTOMERS.get(customer_id)
    if not customer:
        return f"No customer found with ID {customer_id}"
    return(
        f"Customer:{customer['name']}\n"
        f"Email:{customer['email']}\n"
        f"Phone:{customer['phone']}\n"
        f"Account Status:{customer['account_status']}"
    )


//creating and running an agent
//we have system prompt for each agent
SYSTEM_PROMPT="""
you are a customer service agent for an online elctronics store be helpful,professional and concise.use the available tools to look up custom information and process request
Important guidelines:
-Always verify the customer using lookup_customer tool before taking action
-use tool data to answer questions-dont ask for info if you already have
-be warm but efficient
"""

//we give the agent capabilities by configuring with tools as written below
//system prompt sets the behavior and guardrails in natural language
agent=Agent(
    tools=[lookup_customer,get_order_history,process_refund],
    System_prompt=SYSTEM_PROMPT,
)
//calling agent(prompt) runs the full loop and returns a result object
result=agent("Hi ,I am customer c-1001,can you check on my recent orders?")
