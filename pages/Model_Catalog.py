
import streamlit as st, json, os, pandas as pd

st.title("🔍 Model Catalog")
st.caption("Discover approved models with latency, cost, and compliance details")

path = os.path.join("data","model_catalog.json")
with open(path) as f:
    models = json.load(f)
df = pd.DataFrame(models)

# Filters
c1, c2 = st.columns(2)
with c1:
    vendor = st.multiselect("Vendor", sorted(df["vendor"].unique().tolist()), default=df["vendor"].unique().tolist())
with c2:
    approved = st.multiselect("Approval", sorted(df["approved"].astype(str).unique().tolist()), default=df["approved"].astype(str).unique().tolist())

fdf = df[df["vendor"].isin(vendor) & (df["approved"].astype(str).isin(approved))]
st.dataframe(fdf, use_container_width=True)

st.markdown("#### Comparison")
sel = st.multiselect("Compare models", fdf["name"].tolist(), default=fdf["name"].tolist()[:2])
if sel:
    cdf = fdf[fdf["name"].isin(sel)][["name","latency_ms_p50","cost_prompt_per_1k","cost_completion_per_1k"]].set_index("name")
    st.bar_chart(cdf)  # Streamlit bar (acts as placeholder for quick visual)
st.info("This is a mock catalog. In production, this would source from a **Model Registry** with RAI approvals and SLAs.")
