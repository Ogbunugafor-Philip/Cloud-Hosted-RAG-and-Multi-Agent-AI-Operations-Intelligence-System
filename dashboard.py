import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import os
import time

st.set_page_config(page_title="AI Ops Command Center", layout="wide")
API_URL = "http://localhost:8000"
API_KEY = "admin_secret_key_123" 

st.title("🛡️ AI Operations Command Center")

menu = st.sidebar.radio("Navigation", ["Analytics Dashboard", "Interactive Chat", "Secure Document Upload"])

if menu == "Analytics Dashboard":
    st.header("📈 System Performance & Quality")
    latency_df = pd.read_csv("logs/latency_benchmarks.csv") if os.path.exists("logs/latency_benchmarks.csv") else pd.DataFrame()
    ragas_df = pd.read_csv("data/eval/final_ragas_report.csv") if os.path.exists("data/eval/final_ragas_report.csv") else pd.DataFrame()
    kpi1, kpi2, kpi3 = st.columns(3)
    if not latency_df.empty:
        kpi1.metric("Avg Latency", f"{latency_df['latency'].mean():.2f}s")
        kpi2.metric("Total Queries", len(latency_df))
    if not ragas_df.empty:
        kpi3.metric("Avg Faithfulness", f"{ragas_df['faithfulness'].mean():.2f}")
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        if not latency_df.empty:
            st.line_chart(latency_df.set_index('timestamp')['latency'])
    with c2:
        if not ragas_df.empty:
            avg_scores = ragas_df[['faithfulness', 'answer_relevancy', 'context_precision']].mean().reset_index()
            fig = px.bar(avg_scores, x='index', y=0, range_y=[0,1])
            st.plotly_chart(fig, use_container_width=True)

elif menu == "Interactive Chat":
    st.header("💬 AI Operations Assistant")
    query = st.text_input("Ask a question:")
    if st.button("Query AI"):
        headers = {"X-API-KEY": API_KEY}
        res = requests.post(f"{API_URL}/query", json={"query": query}, headers=headers)
        if res.status_code == 200:
            st.info(res.json()['answer'])

elif menu == "Secure Document Upload":
    st.header("🔐 Secure Data Management")
    access_pass = st.text_input("Admin Password", type="password")
    
    if access_pass == "Osita1989":
        st.success("Access Granted")
        
        # Upload Section
        with st.expander("Upload New Document"):
            uploaded_file = st.file_uploader("Select File")
            coll = st.text_input("Collection", value="test_collection")
            if st.button("Ingest"):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
                requests.post(f"{API_URL}/upload", files=files, data={"collection": coll}, headers={"X-API-KEY": API_KEY})
                st.success("Uploaded!")

        st.divider()
        
        # Delete Section
        st.subheader("🗑️ Manage Existing Documents")
        if os.path.exists("data"):
            files_in_dir = [f for f in os.listdir("data") if os.path.isfile(os.path.join("data", f))]
            if files_in_dir:
                for f in files_in_dir:
                    col_file, col_btn = st.columns([3, 1])
                    col_file.write(f)
                    if col_btn.button("Delete", key=f):
                        res = requests.post(f"{API_URL}/delete", data={"filename": f, "collection": "test_collection"}, headers={"X-API-KEY": API_KEY})
                        if res.status_code == 200:
                            st.warning(f"Deleted {f}")
                            time.sleep(1)
                            st.rerun()
            else:
                st.write("No documents found in data/ folder.")
