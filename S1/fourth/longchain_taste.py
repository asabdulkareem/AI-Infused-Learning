from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from common.helper import OPENROUTER_API_KEY, MODEL
from common.web_scraper import fetch_website_contents

prompt = ChatPromptTemplate.from_template("Summarize this website: {content}")
model  = ChatOpenAI(
        temperature=0,
        model=MODEL,
        openai_api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
    )

chain = prompt | model            # "|" = send the prompt INTO the model
print(chain.invoke({"content": fetch_website_contents("google.com")}))  # reuse it for any page!