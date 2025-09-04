import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Customer Service FAQs", layout="wide", initial_sidebar_state="expanded")

# --- TITLE & DESCRIPTION ---
st.title("🤖 **Customer Service FAQ Automation**")
st.markdown("""
This agent automates the handling of frequently asked questions (FAQs) for customers.  
It searches your question for keywords and provides quick answers from a knowledge base.  
""", unsafe_allow_html=True)

# --- FAQ RESPONSE SECTION ---
faq_responses = {
    "hours": "Our customer service hours are Monday to Friday, 9 AM to 5 PM.",
    "return": "You can return items within 30 days of purchase.",
    "shipping": "We offer free shipping for orders over $50.",
    "payment": "We accept Visa, Mastercard, and PayPal."
}

# --- MANUAL INPUT SECTION ---
user_question = st.text_input("Ask a question:")

if user_question:
    response = None
    for keyword, answer in faq_responses.items():
        if keyword.lower() in user_question.lower():  # keyword search
            response = answer
            break

    if response:
        st.markdown("### 📝 **Answer**")
        st.write(response)
    else:
        st.warning("Sorry, I couldn't find an answer to your question.")

    # --- COPY RESPONSE ---
    if response:
        st.markdown("### 📋 **Copy the Answer**")
        st.text_area("Copy this:", response, height=100)
