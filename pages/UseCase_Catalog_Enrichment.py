
import streamlit as st

st.title("Catalog Enrichment — Demo (Mock)")
st.caption("Rewrite titles, normalize attributes, ground to policy")

st.text_area("Raw Title", "🔥 Awesome Bluetooth Earbuds!!! Long Battery + Super Bass 🎧", height=120)
if st.button("Rewrite per Walmart style guide (mock)"):
    st.code("Acme Bluetooth Earbuds, Wireless In‑Ear Headphones, 30‑Hour Battery, Deep Bass, Built‑in Mic, Black", language="markdown")

st.text_area("Raw Attributes", "batteryLife: long; color: jet black; connection: bt5", height=120)
if st.button("Normalize attributes (mock)"):
    st.code("battery_life_hours: 30\ncolor: Black\nbluetooth_version: 5.0", language="markdown")
