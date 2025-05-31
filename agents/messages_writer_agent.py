from openai.agents.conversable import ConversableAgent
from typing import Dict, Any

class MessagesWriterAgent(ConversableAgent):
    def __init__(self):
        super().__init__(
            name="MessagesWriterGPT",
            instructions="""You are a specialized AI for messages writer generation.
            Provide structured, actionable outputs with clear sections."""
        )
    
    async def generate(self, prompt: str) -> Dict[str, Any]:
        response = await self.send_message(
            message=prompt,
            tools=[]
        )
        return {
            "output": response.content,
            "metadata": {"agent": self.name}
        }

