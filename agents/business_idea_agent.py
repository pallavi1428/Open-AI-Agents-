from openai import AsyncOpenAI
from app.config import Config

class BusinessIdeaAgent:
    def __init__(self, config: Config):
        self.config = config
        self.client = AsyncOpenAI(api_key=config.openai_api_key)

    async def generate_idea(self, prompt: str) -> str:
        response = await self.client.chat.completions.create(
            model=self.config.model,
            messages=[
                {
                    "role": "system",
                    "content": "Generate innovative business ideas with: 1) Name 2) One-line pitch 3) Target audience"
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content