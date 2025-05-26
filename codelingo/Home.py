import streamlit as st

st.title("CodeLang - Learn to Code")
st.markdown("**Welcome to CodeLang, where you will be learning the basics of python**")
st.subheader("You will be learning via")
st.markdown("\n <u><b>Flash cards:</u></b> Information cards which will help you understand each topic clearly \n \n <u><b>Question slides:</u></b> Question papers with 2-5 questions on each chapter, there questions will check your understanding", unsafe_allow_html = True)
st.markdown("\n <u><b>Main question slide:</u></b> This slide will contain a multitude of slides and will appear after 5 chapters, each time testing your recall.", unsafe_allow_html = True)

st.write("Do you wish to start the app")
if st.button("Start app"):
    st.switch_page("pages/Lesson1.py")
