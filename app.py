import streamlit as st
from src.data_loader import load_schemes, schemes_to_table
from src.eligibility import filter_schemes

STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
    "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
    "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand",
    "West Bengal", "Andaman and Nicobar Islands", "Chandigarh",
    "Dadra and Nagar Haveli and Daman and Diu", "Delhi", "Jammu and Kashmir",
    "Ladakh", "Lakshadweep", "Puducherry",
]
OCCUPATIONS = ["student", "farmer", "job"]

st.set_page_config(page_title="Welfare Scheme Matcher", page_icon="🇮🇳")

st.title("Welfare Scheme Matcher")
st.write("Find government schemes you may be eligible for.")
st.caption("Eligibility is decided by fixed rules, not by AI. Always check the official link before applying.")

st.header("Your details")

age = st.number_input("Age", min_value=0, max_value=120, value=18, step=1)
income = st.number_input("Family annual income (in rupees)", min_value=0, value=100000, step=10000)
category = st.selectbox("Category", ["General", "OBC", "SC", "ST"])
state = st.selectbox("State / Union Territory", STATES)
occupation = st.selectbox("Occupation", OCCUPATIONS, format_func=str.capitalize)

user = {
    "age": age,
    "income": income,
    "category": category,
    "state": state,
    "occupation": occupation,
}

schemes = load_schemes()
matches = filter_schemes(user, schemes)

st.header("Schemes you may be eligible for")

if not matches:
    st.info("No scheme in our database matches these details yet. We are adding more schemes.")
else:
    st.success(f"Found {len(matches)} matching scheme(s).")
    for scheme in matches:
        with st.expander(scheme["name"], expanded=True):
            st.markdown(f"**Benefit:** {scheme['benefit']}")
            st.markdown("**Documents needed:**")
            for document in scheme["documents"]:
                st.markdown(f"- {document}")
            st.markdown(f"**How to apply:** {scheme['how_to_apply']}")
            st.caption(f"Note: {scheme['notes']}  |  Last verified: {scheme['last_verified']}")
            st.link_button("Open official website", scheme["official_link"])

st.header("All schemes in our database")

table = schemes_to_table(schemes)

st.dataframe(
    table[["name", "type", "benefit", "official_link"]],
    hide_index=True,
    column_config={
        "name": "Scheme",
        "type": "Type",
        "benefit": "Benefit",
        "official_link": st.column_config.LinkColumn("Official link"),
    },
)