
import streamlit as st, json, os, pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Cost & Telemetry")
st.caption("Observe usage, cost, latency, and errors by app/team")

with open(os.path.join("data","telemetry.json")) as f:
    t = pd.DataFrame(json.load(f))
t["date"] = pd.to_datetime(t["date"])

apps = st.multiselect("Apps", sorted(t["app"].unique()), default=sorted(t["app"].unique()))
metric = st.selectbox("Metric", ["cost_usd","tokens_in","tokens_out","latency_ms_p50","errors"], index=0)

ft = t[t["app"].isin(apps)]
pivot = ft.groupby("date").sum(numeric_only=True)

fig = plt.figure()
plt.plot(pivot.index, pivot[metric].values)
plt.title(f"{metric} over time (all selected apps)")
plt.xlabel("Date")
plt.ylabel(metric)
st.pyplot(fig)

st.dataframe(ft.sort_values(["date","app"]), use_container_width=True)
