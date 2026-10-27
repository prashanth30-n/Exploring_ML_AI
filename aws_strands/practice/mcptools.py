# you can connect the agent to different type of tools such as different mcp servers running locally or remotely and ,or define your tools for the agent

# mcp is an open standart way that gives agents to discover and interact with external capabilites like github,aws,databases throught standard protocol
# //servers can runn locally as a subprocess(stdio) or remotely over http


from mcp import stdio_client,StdioServerParameters
from strands import Agent
from strands.tools.mcp import MCPClient
# //defining a mcp server pass the url and strands internally builds the transport layer
aws_knowledge=MCPClient(
    url="https://knowledge-mcp.global.api.aws",
    prefix="knowledge",
)
# //local mcp server using stdio
aws_pricing=MCPClient(
    lambda:stdio_client(StdioServerParameters(
        command="uvx",
        args=["awslabs.aws-pricing-mcp-server@latest"],
        env={"AWS_REGION:"us-east-1""}
    )),
    prefix='pricing'
)
agent=Agent(
    tools=[aws_knowledge,aws_pricing],
    system_prompt="you are an AWS architect"
)
agent("what aws services should i user for a serverless fastapi backend")
# //in the above example mcp servers are used as tools we pass the url and the inbuil strands handles the connecting with the mcp server through mcp protocol and know the agent can use the mcp server,
# there are lot of mcp servers such as github,mongodb,aws,etc

# //The prefix argument namespaces tool names from each server so two servers exposing a tool with the same name don’t collide.
# //tool filtering
# too many tools leads to worse tool selection,hallucinated tool names,and wasted context,in production restrict tools an agent can acess using tool_filters,expose only what agent actually needs

from strands import Agent
from strands.tools.mcp import MCPClient

# //filter to only documentation tools
# //generally a mcp servers has lot of tools so we are limiting what are tools required for the agent to acces,to avoid unncessary tool calls and hallucinations
filtered_mcp=MCPClient(
  url="https://aws-mcp.us-east-1.api.aws/mcp",
   tool_filters={
        "allowed": ["aws___search_documentation", "aws___read_documentation"]
    },
    # //in this we are limiting the this mcp client to only access the required tools for the agent ,there are lot of tools for an mcp server but we are restricing our agent to call them 
    # using tool filters

)
agent=Agent(
    tools=['filtered_mcp']
    system_prompt="you are an aws documentation assistant"
)
