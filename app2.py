import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000/ask"

st.title("🧥 Clothing Review Q&A")
st.write("Ask any question based on clothing reviews!")

# Input
question = st.text_input("Enter your question:")

# When the user clicks the button
if st.button("Submit") and question:
    with st.spinner("Fetching answer..."):
        try:
            response = requests.post(API_URL, json={"question": question})
            if response.status_code == 200:
                result = response.json()
                answer = result.get("answer", "No answer returned.")
                st.success(answer)
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
