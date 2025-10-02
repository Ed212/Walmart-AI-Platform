
import streamlit as st, json, os

st.title("🔒 Guardrails Config")
st.caption("Configure domain-specific filters and safety rules")
path = os.path.join("data","guardrails.json")
with open(path) as f:
    g = json.load(f)

st.checkbox("PII Detection", value=g.get("pii_detection", True))
st.multiselect("Policy Blocks", options=["Self-harm","Hate","Harassment","Sexual content (minors)","Weapons","Finance Scams","Medical Advice"], default=g.get("policy_blocks", []))
st.multiselect("Language Filters", options=["SSN","Credit card","Phone number","Address","Email"], default=g.get("language_filters", []))
st.selectbox("Redaction Mode", options=["mask","drop","hash"], index=["mask","drop","hash"].index(g.get("redaction_mode","mask")))

st.subheader("Hallucination Controls")
st.toggle("Require grounding")
st.toggle("Require citation")

st.info("In production: these settings compile to a **policy engine** that runs pre- and post-generation checks, plus redaction.")
