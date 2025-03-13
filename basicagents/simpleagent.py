import pandas as pd
import os 
from groq import Groq

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_AI_KEY"]=os.getenv("GROQ_API_KEY")

agent=Agent(
    model=Groq(id="qwen-2.5-32b"),
    description="You are an assistance and reply as you asked",
    tools=[DuckDuckGoTools()],
    markdown=True
)

agent.print_response("How many runs were scored by Rohit Sharma in the champions trophy final against NZ")