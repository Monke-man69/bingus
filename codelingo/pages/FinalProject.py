import streamlit as st

st.title("Final project: Python Programming")
st.write("This project will test your understanding of Python programming concepts learned in the previous lessons.")
st.subheader("Project Overview")
st.write("Build a project code with the help of the following modules:")
st.markdown("**1. pandas** ")
st.markdown("**2. numpy** ")
st.markdown("**3. matplotlib**")
st.markdown("**4. math**")
st.markdown("**5. random**")
st.markdown("**6. time**")

st.markdown("You can use one of these or all of these modules in your project to create a project on any topic of your choise. The project should demonstrate your understanding of Python programming concepts, including data manipulation, visualization, and mathematical operations.")

st.subheader("Project Requirements")
st.write("1. Use at least two of the listed modules in your project.")
st.write("2. The project should include data manipulation, visualization, and mathematical operations.")
st.write("3. The project should be well-documented with comments explaining the code.")
st.write("4. The project should be functional and demonstrate the concepts learned in the previous lessons.")

st.subheader("Submission Guidelines")
st.write("1. Submit your project code only as a Python file (.py)")
st.write("2. Ensure your code is well-organized and easy to read.")
st.write("3. Include a brief description of your project and the concepts demonstrated in the code.")

st.subheader("Tips for Success")
st.write("1. Start by planning your project and identifying the modules you want to use.")
st.write("2. Break down your project into smaller tasks and tackle them one at a time.")
st.write("3. Test your code frequently to ensure it works as expected.")
st.write("4. Use online resources and documentation to help you with any challenges you encounter.")
st.write("5. Don't hesitate to ask for help if you're stuck on a problem.")
st.write("6. Have fun and be creative with your project!")

st.subheader("Need Help?")
st.write("If you have any questions or need assistance with your project, refer to the lessons which will be provided at the end of this page")
st.write("You can also send a mail at")
code = ''' sakshamkambast@gmail.com'''
st.code(code, language='python')

st.divider()
if st.button("Go to Extra resources"):
    st.switch_page("pages/ExtraResourcesIndex.py")