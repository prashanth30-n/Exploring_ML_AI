import random
from strands import Agent, tool
from strands.models.ollama import OllamaModel

@tool
def roll_dice(sides: int, count: int = 1) -> str:
    """Roll dice and return the results.

    Args:
        sides: Number of sides on each die (e.g. 6 for a standard die, 20 for a d20)
        count: How many dice to roll
    """
    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls)
    if count == 1:
        return f"🎲 Rolled a d{sides}: {rolls[0]}"
    return f"🎲 Rolled {count}d{sides}: {rolls} (Total: {total})"

# # Before (Ollama, local)
# from strands.models.ollama import OllamaModel
# model = OllamaModel(host="http://localhost:11434", model_id="llama3.1")

# After (Bedrock, cloud)
# from strands.models import BedrockModel
# model=BedrockModel(model_id="us.amazon.nova-2-lite-v1:0")

agent = Agent(
    model=model,
    system_prompt="""You are a dramatic and entertaining tabletop RPG games master.
You narrate scenes vividly and use dice rolls to determine outcomes.
When a player attempts an action that involves chance, roll appropriate dice
and narrate the result. A d20 roll of 15 or higher is generally a success.
Keep responses concise but atmospheric.""",
    tools=[roll_dice],
)
agent("I kick open the tavern door and stride up to the bar. 'Barkeep! Your finest ale!'")