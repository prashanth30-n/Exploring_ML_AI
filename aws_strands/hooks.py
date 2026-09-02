# // to add logging,validation,guardrails,or custom logic at any point in the agent loop,use hooks
# hooks enables use cases such as 
# monitoring the agent
# modifying the tool execution
# adding valiation and error handling
# debuggin complex orchestration patterns


# guardrails are safety controls that sit between users and ai models to keep behaviour safe,accurate,and within definite boundaries


# building a rate limiter hook

from strands import Agent
from strands.hooks import(
    HookProvider,HookRegistry,BeforeInvocationEvent,BeforeToolCallEvent,
)
class RateLimiterHook(HookProvider):
    """Caps each tool at max_calls per agent invocation"""
     def __init__(self, max_calls: int = 3):
        self.max_calls = max_calls
        self.counts: dict[str, int] = {}

    def register_hooks(self, registry: HookRegistry) -> None:
        registry.add_callback(BeforeInvocationEvent, self.reset)
        registry.add_callback(BeforeToolCallEvent, self.check)

    def reset(self, event: BeforeInvocationEvent) -> None:
        """Reset counts at the start of each invocation."""
        self.counts = {}

    def check(self, event: BeforeToolCallEvent) -> None:
        """Enforce the rate limit before each tool call."""
        name = event.tool_use["name"]
        self.counts[name] = self.counts.get(name, 0) + 1
        if self.counts[name] > self.max_calls:
            event.cancel_tool = (
                f"'{name}' hit the {self.max_calls}-call limit. "
                "Do NOT call this tool again."
            )
this is like middleware 
we embed this hook inside the agent as shown below
agent = Agent(
    tools=[lookup_customer, get_order_history, process_refund],
    hooks=[RateLimiterHook(max_calls=3)],
    system_prompt="You are a customer service agent. Be helpful and concise.",
)
