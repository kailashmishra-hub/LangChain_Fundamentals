from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

# Step 1: Create the AI model
model = ChatOpenAI(api_key="Your Api Key", model="gpt-4o-mini")

# Step 2: Create memory
memory = []

# Step 3: First question
memory.append(HumanMessage(content="Explain Gravity in simple words"))

response = model.invoke(memory)

print("AI:", response.content)

# Store AI response in memory
memory.append(AIMessage(content=response.content))

# Step 4: Second question (AI will remember the topic)
memory.append(HumanMessage(content="Give one real-life example"))

response = model.invoke(memory)

print("AI:", response.content)