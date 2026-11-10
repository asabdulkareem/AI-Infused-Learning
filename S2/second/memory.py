from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from common.helper import OPENROUTER_API_KEY, MODEL
from langchain_openai import ChatOpenAI

model  = ChatOpenAI(
        temperature=0,
        model=MODEL,
        openai_api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
    )  #

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly tutor."),     # ① personality, like Class 1
    MessagesPlaceholder("history"),              # ② past turns park here
    ("human", "{question}"),                     # ③ the new question
])
chain = prompt | model

history = [HumanMessage("My name is Aarav."), AIMessage("Hi Aarav!")]
print(chain.invoke({"history": history, "question": "What's my name?"}).content)
# → "Your name is Aarav."  ✅ it "remembered" — because WE re-sent the history