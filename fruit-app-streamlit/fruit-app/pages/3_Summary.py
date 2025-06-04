
import streamlit as st

st.title("Summary")
st.info("This page will show total fruit count and detected categories (mockup).")

# In practice, this would be populated after detection
st.metric("Total Fruits Detected", "86")
st.write("Categories:")
st.write("- Apple: 54")
st.write("- Mango: 32")
