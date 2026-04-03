from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
model = ChatOpenAI(api_key="YOUR API KEY", model="gpt-4o-mini")
template = PromptTemplate( input_variables=["topic"], template="Explain {topic} in simple words.")
filled_prompt = template.format(topic="Gravity")
response = model.invoke(filled_prompt)
print(response.content)
