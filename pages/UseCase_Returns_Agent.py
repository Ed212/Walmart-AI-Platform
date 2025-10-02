
import streamlit as st

st.title("Returns Agent — Demo (Mock)")
st.caption("Policy-aware, empathetic returns with fraud checks")

st.text_area("Context (mock)", "Order #123-4567, delivered 12 days ago, item: BrandX Blender", height=120)
st.text_input("Customer message", "The blender leaks, I'd like to return it.")
if st.button("Respond (mock)"):
    st.code("I'm sorry the blender isn't working as expected. You're within the 30‑day return window. I can issue a prepaid label or exchange for a replacement. Would you prefer a refund or a replacement?", language="markdown")
