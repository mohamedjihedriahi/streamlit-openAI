import openai
import streamlit as st
import os

API_KEY_FILE = ".openai"

def init_openai(api_key):
    openai.api_key = api_key

# Get API key from file
def get_api_key():
    if os.path.exists(API_KEY_FILE):
        with open(API_KEY_FILE, "r") as f:
            return f.read().strip()
    else:
        return None

# Save API key to file
def save_api_key(api_key):
    with open(API_KEY_FILE, "w") as f:
        f.write(api_key)

# Change API key
def change_api_key():
    new_key=st.text_input("Enter your OpenAI API key:", type="password")
    if st.button("Save new API key"):
        os.remove(API_KEY_FILE)
        init_openai(new_key)
        save_api_key(new_key)
        st.session_state["page"] = "page1"
        

def chat_prompt():
    st.write("# OpenAI Demo")
    if st.button("Go to settings"):
        st.session_state["page"] = "page2"
    max_tokens = st.slider("Select max tokens value:", 100, 4096, key="max_tokens_slider")
    st.write("You selected:", max_tokens)
    temperature = st.slider("Select temperature value:", 0.0, 1.0, step=0.1, key="temperature_slider")
    st.write("You selected:", temperature)
    question = st.text_input("Ask me a question : ")
    if (len(question) + max_tokens > 4096):
        max_tokens = 4096 - len(question)
    if st.button("Get answer"):
        response = openai.Completion.create(
            engine="text-davinci-003", prompt=question, max_tokens=max_tokens - 1, stop=None, temperature=temperature
        )
        st.session_state["answer"] = response.choices[0].text
    if "answer" in st.session_state:
        st.write(st.session_state["answer"])

    


# Define page functions
def page1():
    api_key = get_api_key()
    if api_key:
        init_openai(api_key)
        chat_prompt()
    else:
        st.write("# Hello!")
        api_key = st.text_input("Enter your OpenAI API key:", type="password")
        if st.button("Save API key"):
            init_openai(api_key)
            save_api_key(api_key)
            st.write("API key saved.")
            st.empty()
            st.empty()
            st.empty()
            chat_prompt()
    

def page2():
    st.write("# Settings")
    change_api_key()
    if st.button("Return to main"):
        st.session_state["page"] = "page1"

# Define app
def main():
    pages = {"page1": page1, "page2": page2}
    if "page" not in st.session_state:
        st.session_state["page"] = "page1"
    page = pages[st.session_state["page"]]
    page()

if __name__ == "__main__":
    main()
