from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
from agents import agent
import asyncio

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

#Reference: https://ai.google.dev/gemini-api/docs/openai
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

my_agent = agent(instructions="You are a helpful agent")

async def main():
    result = Runner.run(agent, "What is the capital of France?")
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())