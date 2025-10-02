
import streamlit as st

st.title("Shopper Assistant — Demo (Mock)")
st.caption("Conversational shopping: size & fit with inventory awareness")

st.text_area("Context (mock)", "User: returning customer\nHeight: 5'10\"; Weight: 170lb\nPrior purchases: BrandX M Tshirt, BrandY 32x32 Jeans\nInventory: Nearby store has S/M/L", height=150)
st.text_input("User message", "Looking for a rain jacket I can hike in—prefer light and breathable.")
if st.button("Run (mock)"):
    st.code("I'd recommend the BrandX TrailShell. Based on your fit history, size M should work. Nearby store (MV) has 3 in stock. Want me to hold one or ship?", language="markdown")
