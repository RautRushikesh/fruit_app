
import streamlit as st

st.title("Yield Estimation")

fruit_type = st.selectbox("Select Fruit Type", ["apple", "mango", "orange"])
count = st.number_input("Enter total fruit count", min_value=0)

weights = {
    'apple': 0.18,
    'mango': 0.25,
    'orange': 0.20
}

if st.button("Estimate Yield"):
    weight = weights.get(fruit_type, 0.2)
    yield_kg = count * weight
    st.success(f"Estimated Yield: {yield_kg:.2f} kg")
