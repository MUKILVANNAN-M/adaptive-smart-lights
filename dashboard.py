import streamlit as st
import random

st.title("💡 Smart Adaptive Lights Dashboard")

st.write("Real-time energy consumption and streetlight status")

lights = ["Light 1", "Light 2", "Light 3", "Light 4"]

for light in lights:
    status = random.choice(["ON", "DIM"])
    energy = random.uniform(2, 10)

    st.write(f"{light} → Status: {status}, Energy: {round(energy, 2)} units")
