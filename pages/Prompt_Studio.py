
import streamlit as st, json, os, pandas as pd
from datetime import datetime

st.title("🎯 Prompt Studio")
st.caption("Test prompts across models, version, and compare outputs")

# Load prompts
with open(os.path.join("data","prompts.json")) as f:
    library = json.load(f)
lib_df = pd.DataFrame(library)

use_case = st.selectbox("Use case", sorted(lib_df["use_case"].unique()))
filtered = lib_df[lib_df["use_case"]==use_case]

col1, col2 = st.columns([2,1])
with col1:
    prompt = st.text_area("Prompt", filtered.iloc[0]["prompt"] if not filtered.empty else "", height=180)
with col2:
    model = st.selectbox("Model", ["GPT-4o","Claude 3.5 Sonnet","Llama 3.1 70B","Mistral Large 2"])
    temperature = st.slider("Temperature", 0.0, 1.0, 0.2, 0.05)
    max_tokens = st.slider("Max Tokens", 64, 2048, 256, 32)

if st.button("Run (mock)"):
    st.success("Ran prompt against selected model (mock).")
    st.code(f"[{model}] → Synthetic output for '{use_case}' generated here.\n(Replace with real API call.)")

st.markdown("#### Library")
st.dataframe(lib_df, use_container_width=True)
st.caption("Tip: Add A/B prompt versions and save as templates for teams.")
