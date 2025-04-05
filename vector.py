from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("Clothing review.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        if pd.isna(row["Review Text"]):
         continue

        document = Document(
            page_content=row["Review Text"],
            metadata={"rating": row["Rating"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

    print(f"Number of valid documents to add: {len(documents)}")

    #for i, row in df.iterrows():
    #    document = Document(
     #       page_content=row["Review Text"],    
      #      metadata={"rating": row["Rating"]},
       #     id=str(i)
        #)
        #ids.append(str(i))
        #documents.append(document)
        
vector_store = Chroma(
    collection_name="clothing_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

print("Documents successfully added to Chroma.")
    
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)