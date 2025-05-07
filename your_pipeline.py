
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
import pandas as pd
import os

model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about clothing pieces.

Here are some relevant reviews: 
{reviews}

Here is the question to answer: 
{question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# CSV file to save history
CSV_FILE = "qa_history.csv"


if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["Question", "Answer"])
    df.to_csv(CSV_FILE, index=False)

def ask_question(user_question):
    docs = retriever.invoke(user_question)
    reviews = "\n\n".join([doc.page_content for doc in docs])
    answer = chain.invoke({"reviews": reviews, "question": user_question})

   
    save_to_csv(user_question, answer)

    return answer

def save_to_csv(question, answer):
    df = pd.DataFrame([[question, answer]], columns=["Question", "Answer"])
    df.to_csv(CSV_FILE, mode="a", header=False, index=False)
