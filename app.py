import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import streamlit as st

load_dotenv()

st.title("Chapter 6 【提出課題】LLM機能を搭載したWebアプリ")
st.write("選択した専門家に質問ができます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["料理の領域の専門家", "AIの領域の専門家"]
)

st.divider()

if selected_item == "料理の領域の専門家":
    input_message = st.text_input(label="料理に関する質問を入力してください。")
    text_Q = input_message

else:
    input_message = st.text_input(label="AIに関する質問を入力してください。")
    text_Q = input_message

if st.button("実行"):
    st.divider()

    if selected_item == "料理の領域の専門家":
        if input_message:
            st.write(f"質問: **{text_Q}**")

        else:
            st.error("テキストを入力してから「実行」ボタンを押してください。")

    else:
        if input_message:
            st.write(f"質問: **{text_Q}**")
        else:
            st.error("テキストを入力してから「実行」ボタンを押してください。")

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

messages = [

    SystemMessage(content="You are a helpful assistant."),

    HumanMessage(text_Q),

]

result = llm(messages)

print(result.content)

st.write(f"回答: **{result.content}**")
