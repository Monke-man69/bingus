import streamlit as st

st.title("🎓 Lesson 1: Basics of python")
st.write("Lets learn the basics of python")

code_example = '''x = 5
print(x)'''

st.code(code_example, language='python')

st.write("Try questions now?")
st.page_link("pages/Lesson1questions.py", label="Questions for Lesson 1")