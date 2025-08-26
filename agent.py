from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled

set_tracing_disabled(True)

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

#Reference: https://ai.google.dev/gemini-api/docs/openai
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client
)

my_agent: Agent = Agent(
    name="Openai Assistant",
    model=model, 
    instructions="You are a helpful assistant"
)

result = Runner.run_sync(my_agent, "What is the capital of France?")