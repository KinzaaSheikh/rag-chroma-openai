import chromadb
from dotenv import load_dotenv
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from openai import AsyncOpenAI
import uuid

# gemini_api_key = os.getenv("GEMINI_API_KEY")
# load_dotenv()


# # Tracing disabled
# set_tracing_disabled(disabled=True)

# # 1. Which LLM Service?
# external_client: AsyncOpenAI = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# # 2. Which LLM Model?
# llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
#     model="gemini-2.5-flash",
#     openai_client=external_client
# )

client = chromadb.Client()

collection = client.create_collection(name="exam_info")

with open("clues.txt", "r", encoding="utf-8") as text:
    content = text.read().splitlines()

collection.upsert(
    ids=[str(uuid.uuid4()) for _ in content],
    documents=content, 
    metadatas=[{"line": line} for line in range(len(content))]
)

print(collection.peek())


# agent = Agent(
#     name = "Document Query Agent",
#     instructions="You are a helpful agent that only uses context to answer queries related to learning roadmap"
# )
