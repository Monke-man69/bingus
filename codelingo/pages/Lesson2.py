import streamlit as st

st.title("🎓 Lesson 1: Variables")
st.write("Let's learn how to use variables in Python.")

code_example = '''x = 5
print(x)'''

st.code(code_example, language='python')

st.write("Try questions now?")
if st.button("Questions for Lesson 2"):
    st.switch_page("pages/Lesson2questions.py")