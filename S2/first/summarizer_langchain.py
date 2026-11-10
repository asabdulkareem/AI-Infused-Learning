from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from common.helper import OPENROUTER_API_KEY, MODEL
from common.web_scraper import fetch_website_contents   # reuse Class 1's scraper

prompt = ChatPromptTemplate.from_template(            # ①
    "Give a short, friendly summary of this website:\n\n{website}")

model  = ChatOpenAI(
        temperature=0,
        model=MODEL,
        openai_api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
    )  # ②

parser = StrOutputParser()                             # ③

chain = prompt | model | parser                        # ④

def summarize(url):
    return chain.invoke({"website": fetch_website_contents(url)})   # ⑤

print(summarize("https://anthropic.com"))