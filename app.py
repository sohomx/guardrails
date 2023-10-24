import streamlit as st
import os
from dotenv import load_dotenv
import openai

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

def without_guardrails(text):
    response = openai.Completion.create(
        prompt="Translate the texts to English Language\n"+text,
        engine="text-davinci-003",
        max_tokens=2048,
        temperature=0
    )
    result = response['choices'][0]['text']
    return result

def main():

    st.title("Guardrails Implementation in LLMs")

    text_area = st.text_area("Enter your text that you want to translate!")

    if st.button("Translate"):
        if len(text_area) > 0:
            st.info(text_area)

            st.warning("Translation response without guardrails")
            without_guardrails_result = without_guardrails(text_area)
            st.success(without_guardrails_result)

if __name__ == "__main__":
    main()