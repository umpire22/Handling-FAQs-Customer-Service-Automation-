import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Customer Service FAQs", layout="wide", initial_sidebar_state="expanded")

# --- TITLE & DESCRIPTION ---
st.title("🤖 **Customer Service FAQ Automation**")
st.markdown("""
This agent automates the handling of frequently asked questions (FAQs) for customers. It can quickly provide answers from a knowledge base. 
Simply type a question and get an instant response.
""", unsafe_allow_html=True)

# --- MANUAL INPUT SECTION ---
user_question = st.text_input("Ask a question:")

# --- FAQ RESPONSE SECTION ---
faq_responses = {
    "hours": "Our customer service hours are Monday to Friday, 9 AM to 5 PM.",
    "return policy": "You can return items within 30 days of purchase.",
    "shipping": "We offer free shipping for orders over $50."
}

if user_question:
    response = faq_responses.get(user_question.lower(), "Sorry, I couldn't find an answer to your question.")
    st.markdown(f"### 📝 **Answer**")
    st.write(response)

    # --- COPY RESPONSE ---
    st.markdown("### 📋 **Copy the Answer**")
    st.text_area("Copy this:", response, height=100)

# --- STYLING ---
st.markdown("""
    <style>
    body {
        background-color: #1e1e1e;
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    .stTextInput, .stTextArea {
        background-color: #333;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)
