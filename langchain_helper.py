from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts.chat import ChatPromptTemplate

load_dotenv()

parser = StrOutputParser()
model = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)

template = "I have a {animal} pet of {breed} breed and is {color} color. Give me a list of cool names for it."

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model | parser

def get_pet_name(animal, breed, color):

  name = chain.invoke({"animal": "animal",
                       "breed": "breed",
                       "color": "color"})

  return name

if __name__ == "__main__":
  print(get_pet_name("cat", "tabby", "brown"))