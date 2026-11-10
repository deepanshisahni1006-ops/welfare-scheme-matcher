import streamlit as st

st.set_page_config(page_title="Welfare Scheme Matcher", page_icon="🇮🇳")

st.title("Welfare Scheme Matcher")
st.write("Find government schemes you may be eligible for.")
st.caption("Eligibility is decided by fixed rules, not by AI. Always check the official link before applying.")

st.header("Your details")

age = st.number_input("Age", min_value=0, max_value=120, value=18, step=1)
income = st.number_input("Family annual income (in rupees)", min_value=0, value=100000, step=10000)
category = st.selectbox("Category", ["General", "OBC", "SC", "ST"])

st.write(f"You entered: age {age}, income Rs {income}, category {category}.")