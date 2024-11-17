import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBL7YBM6zc7SNlKIhPhHR7PGAK2FQZIBj0")

model = genai.GenerativeModel("models/gemini-1.5-flash")

st.title("AI Code Reviewer - Python Code Review")
st.markdown("Paste your Python code below, and I will review it for potential bugs and improvements.")

code_input = st.text_area("Enter your Python code here:", height=300)

review_output = None

def review_code(code):
    prompt = f"Review the following Python code for errors, bugs, or areas of improvement. Provide a bug report, suggested fixes, and an explanation of what was wrong:\n\n{code}"

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if st.button("Submit Code for Review"):
    if code_input:
        st.subheader("AI Code Review:")
        review_output = review_code(code_input)  
        st.write(review_output)
    else:
        st.warning("Please paste some Python code above to get a review.")

if review_output is not None:
    st.download_button(
        label="Download Fixed Code",
        data=review_output,
        file_name="reviewed_code.py",
        mime="text/x-python-script"
    )
