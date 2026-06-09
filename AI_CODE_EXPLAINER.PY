import google.generativeai as genai
import streamlit as st
genai.configure(api_key="YOUR_API_KEY")
model=genai.GenerativeModel("gemini-2.5-flash")
prompt=st.text_input("AI CODE EXPLAINER 🤖")
uh =("You are a AI Code Explainer. You need to explain the code based on the given topic or prompts. ")
if st.button("submit"):
    response = model.generate_content(prompt+uh)
    st.write(response.text)




# py -m pip install streamlit
#py -m pip install google generativeai