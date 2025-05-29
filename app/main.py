import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))


import asyncio
from .runner import Runner  # Changed to relative import

async def main():
    runner = Runner()
    idea = await runner.generate("eco-friendly products for urban millennials")
    print("Generated Idea:\n", idea)

if __name__ == "__main__":
    asyncio.run(main())