from openai.agents.conversable import ConversableAgent
from typing import Dict, Any

class EmailWriterAgent(ConversableAgent):
    def __init__(self):
        super().__init__(
            name="EmailWriterGPT",
            instructions="""You are a specialized AI for email writer generation.
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

