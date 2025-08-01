import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from Secret_Key import gemini_api_key

# Initialize Gemini via LangChain
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-pro",
    temperature=0.7,
    google_api_key=gemini_api_key
)

# Streamlit UI
st.set_page_config(page_title="India Travel Planner", page_icon="🌍")
st.title("🌴 Best Time to Travel in India")
st.caption("Powered by Gemini AI + LangChain")

month = st.selectbox("📅 Select a Travel Month", [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
])

if st.button("✨ Show Best Places"):
    with st.spinner("Finding the perfect destinations..."):
        prompt = f"""
        I'm planning to travel in India during {month}.
        Suggest me the best regions or states to visit, and for each region, list 2-3 famous tourist places.
        Also add a short 2-line travel tip for the month.
        Format output in markdown:
        - State/Region
          - Place 1
          - Place 2
        """
        response = llm.invoke(prompt)
        st.markdown(response.content)

