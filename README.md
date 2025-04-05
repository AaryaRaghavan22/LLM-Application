# LLM-Application
This project is an interactive question-answering system built with LangChain, Ollama, and Chroma vector store. It allows users to ask questions about clothing based on real customer reviews.

# 🧠 Clothing Review Q&A System

This is a terminal-based question-answering system built using **LangChain**, **Ollama**, and **Chroma vector store**. It allows users to ask natural language questions about clothing products, with answers generated based on actual customer reviews.

---

## 📌 Features

- 🔍 **Semantic Search**: Retrieves the most relevant reviews using vector similarity search with Chroma.
- 🤖 **LLM-Powered Responses**: Uses `llama3.2` via Ollama to generate natural, context-aware answers.
- 🧾 **Review-Based Reasoning**: Answers are grounded in real customer feedback from a CSV dataset.
- 💬 **Interactive Q&A Interface**: Runs in the terminal and responds to your queries in real-time.

---

## 🛠️ Tech Stack

- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/) (`llama3.2` and `mxbai-embed-large`)
- [Chroma](https://www.trychroma.com/) for vector database
- `pandas` for CSV handling

---

## 📂 Project Structure


---

## 🚀 How It Works

1. **Embeddings**: Reads reviews from `Clothing review.csv` and embeds them using `mxbai-embed-large`.
2. **Vector Store**: Stores these embeddings in a Chroma vector database.
3. **Retrieval**: When a user asks a question, it retrieves the most relevant reviews.
4. **Response Generation**: The question and reviews are passed to `llama3.2` via Ollama to generate a final answer.

---

## 🧪 Example Use

```bash
$ python main.py

Ask your question (q to quit): What do people say about the sizing?

AI: Most reviewers mention that the sizing runs slightly small. Consider ordering one size up.


