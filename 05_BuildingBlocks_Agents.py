import os
import requests
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent

os.environ[
    "OPENAI_API_KEY"] = ""  # Replace with your OpenAI key

#Create a tool
@tool
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

@tool
def substract_numbers(a: int, b: int) -> int:
    """Subtracts two numbers."""
    return a - b

@tool
def temp_conv(f:int) -> float:
    """Converts a temperature to a Celsius."""
    c=5*((f-32)/9)
    return c

@tool
def capital(str1: str) -> str:
    """Returns the capital city of a given country."""
    url = f"https://restcountries.com/v3.1/name/{str1}"
    response = requests.get(url)
    data = response.json()
    return(data[0]["capital"][0])


model = ChatOpenAI(model="gpt-4o-mini")

# Create the agent
agent = create_agent(
    model=model,
    tools=[add_numbers,substract_numbers, temp_conv,capital],
    system_prompt = "You must answer questions only using the provided tools. If the required tool is not available, say that you dont have available tools to answer that.")

# Ask a question
response = agent.invoke(
    {"messages": [("user", "What is the capital of Brazil?")]}
)
print(response)
print(response["messages"][-1].content)