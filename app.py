import streamlit as st

from src.answer_generator import generate_answer

st.title("Resume questions app")

st.write("Ask a question about Paul's work experience...")

question = st.text_input("Enter your question:")

if "answer" not in st.session_state:
    st.session_state.answer = ""

if st.button("Ask"):
    if question.strip():
        with st.spinner("Generating answer..."):
            st.session_state.answer = generate_answer(question)
    else:
        st.warning("please enter a question.")

st.subheader("Answer")
st.text_area(
    "Generated Answer",
    value = st.session_state.answer,
    height = 200,
    disabled = True,
)

