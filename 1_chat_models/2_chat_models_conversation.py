from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()

llm =  ChatOpenAI(model="gpt-4o-mini")

messages = [
SystemMessage("You are an expert in social media content strategy"),
HumanMessage("Give a short tip to create engagings posts on intagram")
]

result = llm.invoke(messages)

print(result.content)