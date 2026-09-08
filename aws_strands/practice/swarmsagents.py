# a swarm  creates autonomous agent teams that dynamically coordinate through  shared memory ,allowing multiple specialistes to collaborate on complex tasks ,think
#of it is as brainstorming seesion where experts build on each others ideas ,with the team  self organising  to deliver best collective results
import logging
from strands import Agent
from strands.multiagent import Swarm
from strands_tools import memory,calculator,file_write

#enables strands debug logs level and prints to terminal
logging.getLogger("strands.multiagent").setLevel(logging.DEBUG)
logging.basicConfig(
     format="%(levelname)s | %(name)s | %(message)s", 
    handlers=[logging.StreamHandler()]
)
researcher=Agent(
    name="researcher",
    system_prompt="You research topics thoroughly using your memory and built-in knowledge", 
    tools=[memory] 

)
analyst=Agent(
    name="analyst",
    system_prompt="you analyse the data and create insights"
    tools=[calculator,memory]
)
writer=Agent(
    name="writer",
    system_prompt="you write comprehensive reports based on research and analysis",
    tools=[file_write,memory]
)
#swarms automatically coordinates agents 
market_research_team=Swarm(
    [researcher,analyst,writer]
)
result=market_research_team(
    "What is the history of AI since 1950? Create a comprehensive report" 
)