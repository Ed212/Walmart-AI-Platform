
import streamlit as st
from datetime import datetime
import json, os, pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Walmart AI Platform — Prototype", layout="wide")

st.markdown("# Walmart AI Platform — Prototype")
st.caption("Vertical slice: Model Catalog • Prompt Studio • Guardrails • Cost Insights • Deployment • Feedback")

st.info("This is a UI **mockup** with simulated data to demonstrate the experience and architecture pattern.")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Active Apps", 4, delta="+1 WoW")
with col2:
    st.metric("Total Cost (7d)", "$7,877", delta="-6%")
with col3:
    st.metric("Median Latency", "409 ms", delta="-4%")
with col4:
    st.metric("Guardrail Blocks (7d)", 37, delta="-12%")

st.markdown("### Quick Links")
st.link_button("🔍 Model Catalog", "Model_Catalog")
st.link_button("🎯 Prompt Studio", "Prompt_Studio")
st.link_button("🔒 Guardrails Config", "Guardrails_Config")
st.link_button("📊 Cost & Telemetry", "Cost_&_Telemetry")
st.link_button("🚀 Deployment", "Deployment_SDK")
st.link_button("📝 Feedback Loop", "Feedback_Loop")

# Use case cards
st.markdown("### Featured Use Cases")
uc1, uc2, uc3, uc4 = st.columns(4)
for i, (col, title, desc) in enumerate([
    (uc1, "Seller Assistant", "Summarize GMV, flag anomalies, recommend actions"),
    (uc2, "Shopper Assistant", "Conversational shopping with size fit & availability"),
    (uc3, "Catalog Enrichment", "Rewrite titles, normalize attributes, ground to policy"),
    (uc4, "Returns Agent", "Policy-aware returns with empathy and fraud checks"),
]):
    with col:
        st.subheader(title)
        st.caption(desc)
        st.page_link(f"pages/UseCase_{title.replace(' ', '_')}.py", label="Open")

# Simple cost trend chart (matplotlib, single plot)
telemetry_path = os.path.join("data","telemetry.json")
if os.path.exists(telemetry_path):
    with open(telemetry_path) as f:
        t = pd.DataFrame(json.load(f))
    t["date"] = pd.to_datetime(t["date"])
    fig = plt.figure()
    for app in t["app"].unique():
        subset = t[t["app"]==app].groupby("date").sum(numeric_only=True)["cost_usd"]
        plt.plot(subset.index, subset.values, label=app)
    plt.title("Cost by App Over Time")
    plt.xlabel("Date")
    plt.ylabel("USD")
    plt.legend()
    st.pyplot(fig)
else:
    st.warning("Telemetry not found")
