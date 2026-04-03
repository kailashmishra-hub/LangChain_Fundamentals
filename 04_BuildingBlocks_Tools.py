from langchain_core.tools import tool
## Structure of tool
# @tool
# def function_name(input: type) -> return_type:

@tool
def calculator(a:int,b:int) -> int:
    """Adds two numbers and returns the result."""
    return a+b

results = calculator.invoke({"a":5,"b":6})
print(results)