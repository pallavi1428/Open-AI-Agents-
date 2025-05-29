from agents.business_idea_agent import BusinessIdeaAgent
from app.config import Config

class Runner:
    def __init__(self):
        self.config = Config()
    
    async def generate(self, prompt: str) -> str:
        agent = BusinessIdeaAgent(self.config)
        return await agent.generate_idea(prompt)