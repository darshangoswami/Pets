from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

parser = StrOutputParser()
model = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)

chain = model | parser

def get_pet_name():

  name = chain.invoke("Give me a list of cool names")

  return name

if __name__ == "__main__":
  print(get_pet_name())