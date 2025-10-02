
import streamlit as st

st.title("📝 Feedback Loop")
st.caption("Collect human ratings and comments to steer model improvements")

col1, col2 = st.columns(2)
with col1:
    st.text_area("Model Output (mock)", "Here's an example response from the Seller Assistant...")
with col2:
    rating = st.radio("Rating", ["👍","👎"])
    comment = st.text_area("Comment", placeholder="What was helpful or off?")

if st.button("Submit Feedback (mock)"):
    st.success("Feedback recorded (mock). In production, this writes to a training signal store.")
