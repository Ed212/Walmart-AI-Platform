
import streamlit as st

st.title("Seller Assistant — Demo (Mock)")
st.caption("Summarizes seller GMV, flags anomalies, and recommends actions")

st.text_area("Context (mock)", "Seller: ACME Outdoors\nYesterday GMV: $92,340 (+12%)\nAd spend: $7,210\nTop SKUs: ...", height=150)
st.text_area("User Prompt", "How did we perform yesterday and what should I do today?")
if st.button("Run (mock)"):
    st.code("Performance looks strong: +12% GMV day-over-day. ROAS: 12.8. Two SKUs stockout risk.\nActions: 1) Increase budget +8% on top performer. 2) Replenish SKU-123, SKU-456. 3) Add 2P offers where margin permits.", language="markdown")
