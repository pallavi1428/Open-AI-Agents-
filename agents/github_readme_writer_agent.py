from openai.agents.conversable import ConversableAgent
from typing import Dict, Any

class GithubReadmeWriterAgent(ConversableAgent):
    def __init__(self):
        super().__init__(
            name="GithubReadmeWriterGPT",
            instructions="""You are a specialized AI for github readme writer generation.
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

