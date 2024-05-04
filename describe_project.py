import os
from typing import List

from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI, OpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

load_dotenv()

llm = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"])

DESCRIBE_PROMPT_TEMPLATE = """
    Describe the following piece of code:
    {code}
    
    Generate an high level and concise description of the code, explain it to technical people.
"""


def generate_description(filename: str) -> List[str]:
    print(f"generating description for file {filename}")
    loader = TextLoader(filename)
    raw_documents = [d.page_content for d in loader.load()]

    python_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON, chunk_size=4000, chunk_overlap=0
    )
    code_documents = python_splitter.create_documents(raw_documents)

    describe_chain = LLMChain(llm=llm,
                              prompt=PromptTemplate(template=DESCRIBE_PROMPT_TEMPLATE, input_variables=["code"]))

    describe_result = list()
    for d in code_documents:
        describe_result.append(describe_chain.invoke(input={"code": d}).get("text"))
    return describe_result


def do_describe_folder(root_folder):
    descriptions_set = dict()
    for root_folder, dirs, files in os.walk(root_folder):
        for filename in files:
            if filename == "__init__.py":
                continue

            full_filename = str(os.path.join(root_folder, filename))
            filename_descriptions: List[str] = generate_description(full_filename)
            print(f"filename descriptions for file {filename} is {filename_descriptions}")
            descriptions_set[filename] = filename_descriptions
    return descriptions_set


if __name__ == '__main__':
    descriptions = do_describe_folder("../app/service/kafka")
