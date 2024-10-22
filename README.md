# AI Text Summarizer
```
AI Text Summarizer App- built using Using Langchain 🦜🔗, OpenAI and Streamlit 👑
```

## AI Text Summarizer Overview

- Please review requirements.txt file in the project for the required libraries.
- The app accepts paragraph of text as input (text to be summarized).
- The input text is split into chunks using `CharacterTextSplitter()` along with its `split_text()` method.
- A document is generated via `Document()` method.
- AI text summarization is achieved using `load_summarize_chain()` by applying the `invoke()` method on the input `docs`.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-text-summarizer.streamlit.app/)

## Required- OpenAI API key

Get your own OpenAI API key by following the instructions below-

1. Go to https://platform.openai.com/account/api-keys
2. Login or Signup for a new account.
2. Click on the `+ Create new secret key` button.
3. Enter the name of the key which is optional.
4. Select a project or let it be Default project.
5. Click `Create Secret Key`.
