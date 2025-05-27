import streamlit as st

st.title("INDEX FOR CODING LESSONS")
st.write("Welcome to the index page for coding lessons. Here you can navigate to different lessons and their respective questions.")
st.subheader("Available Lessons:")
st.markdown("- [Lesson 1: Basics of Python](pages/Lesson1.py)")
if st.button("Start lesson 1"):
    st.switch_page("pages/Lesson1.py")
st.markdown("- [Lesson 2: Variables](pages/Lesson2.py)")
if st.button("Start lesson 2"):
    st.switch_page("pages/Lesson2.py")
st.markdown("- [Lesson 3: Data Types](pages/Lesson3.py)")
if st.button("Start lesson 3"):
    st.switch_page("pages/Lesson3.py")
st.markdown("- [Lesson 4: Control Structures](pages/Lesson4.py)")
if st.button("Start lesson 4"):
    st.switch_page("pages/Lesson4.py")
st.markdown("- [Lesson 5: Functions](pages/Lesson5.py)")
if st.button("Start lesson 5"):
    st.switch_page("pages/Lesson5.py")
st.markdown("- [Lesson 6: Modules](pages/Lesson6.py)")
if st.button("Start lesson 6"):
    st.switch_page("pages/Lesson6.py")
st.markdown("- [Lesson 7: File Handling](pages/Lesson7.py)")
if st.button("Start lesson 7"):
    st.switch_page("pages/Lesson7.py")
st.markdown("- [Lesson 8: Error Handling](pages/Lesson8.py)")
if st.button("Start lesson 8"):
    st.switch_page("pages/Lesson8.py")
st.markdown("- [Lesson 9: Object-Oriented Programming](pages/Lesson9.py)")
if st.button("Start lesson 9"):
    st.switch_page("pages/Lesson9.py")
st.markdown("- [Lesson 10: Advanced Topics](pages/Lesson10.py)")
if st.button("Start lesson 10"):
    st.switch_page("pages/Lesson10.py")