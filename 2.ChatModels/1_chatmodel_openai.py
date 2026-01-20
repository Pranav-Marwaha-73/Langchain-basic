from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 
import os

load_dotenv()
model = ChatOpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-120b"
)
result=model.invoke("What is capital of India")
print(result.content)