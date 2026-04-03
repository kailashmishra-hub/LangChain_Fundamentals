from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Step 1: Create the AI model
model = ChatOpenAI(api_key="Your api key", model="gpt-4o-mini")

# Step 2: Create a prompt template
template = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple words.Do not repeat the same topic"
)

# Step 3: Create a chain
chain = template | model

# Step 4: Run the chain
topics = ["Gravity", "Cricket" , "Football"]
for topic in topics:
    response = chain.invoke({"topic": topic})
    print(response.content)
    print("*" * 200)

#print(response.content)