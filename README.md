# OpenAI Demo
This is a simple [Streamlit](https://streamlit.io/) app that uses the [OpenAI API](https://platform.openai.com/docs/guides/chat/introduction) to answer questions.
<p>
  <a href="https://github.com/topics/python"><img src="images/python.png" height="50" hspace="10"/></a>
  <a href= "https://streamlit.io/"><img src="images/streamlit.jpg" height="50" hspace="10"/> </a>
  <a href = "https://platform.openai.com/docs/guides/chat/introduction"><img src="images/openai.png" height="50" hspace="10"/></a>
</p>

## Prerequisites
Before running the app, you need to have Docker installed on your machine.
To use this app, you will need an OpenAI API key. You can get one by signing up at the OpenAI website.
>  To change the OpenAI API key used by the app, follow the steps below:
> > Delete /app/.opeanai and refresh the page
> > or change it from the UI
## Usage
### Locally
#### Installation
To install the dependencies for this app, run the following command:
```bash
cd app
pip install -r requirements.txt
```
#### Usage
To run the app, use the following command:
```bash
streamlit run app.py
```
When you run the app for the first time, you will be prompted to enter your OpenAI API key. If you don't have one, you can sign up at the OpenAI website.

Once you have entered your API key, you can start asking questions by typing them into the text box and pressing the "Obtenir une réponse d'OpenAI" button. The app will use the OpenAI API to generate a response, which will be displayed on the screen.


- **app.py**: This is the main Python script that runs the Streamlit app.
- **requirements.txt**: This file contains the list of dependencies required to run the app.

## Demo
![Demo](images/gif.gif)

