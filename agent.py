# type: ignore

from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool
from db.vectorstores import vector_db 
from mem0 import MemoryClient



set_tracing_disabled(True)

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

mem0 = MemoryClient()

# Create two memory tools: save and recall
@function_tool
def add_memory(query: str, user_id: str) -> str:
    return mem0.add([{"role": "user", "content": query}], user_id=user_id)

@function_tool
def search_memory(query: str, user_id: str) -> str:
    return mem0.search(query, user_id=user_id, limit=3)

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
    # tools=["vector_db"] 
    instructions="You are a helpful assistant"
)


agent = Agent(
    name="Memory Assistant",
    instructions="""You are a helpful assistant with memory.
    Always check memory first before answering.
    Save new details about the user whenever possible.""",
    tools=[search_memory, add_memory],
    model=llm_model,
)

result = Runner.run_sync(my_agent, "What is the capital of France?")