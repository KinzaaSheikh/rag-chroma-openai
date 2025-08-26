from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
from agents import Agent, Runner
import asyncio

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

#Reference: https://ai.google.dev/gemini-api/docs/openai
# client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

async def main():
    my_agent = Agent(
    name="Openai Assistant",
    model="litellm/gemini/gemini-2.5-flash-preview-04-17"
    )

    result = await Runner.run(my_agent, input="What's the capital of France?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())