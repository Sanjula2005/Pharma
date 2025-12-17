import streamlit as st
from master_agent import MasterAgent
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Agentic Pharma AI", layout="wide")

st.title("💊 Agentic AI Pharma Innovation Tool")

user_query = st.text_area("Enter your molecule or research question:")

if st.button("Run Analysis"):
    with st.spinner("Running agentic workflow..."):
        master = MasterAgent()
        report_path = master.run(user_query)
        st.success("✅ Report generated successfully!")
        st.download_button("Download Report", open(report_path, "rb"), file_name="Product_Story.pdf")
