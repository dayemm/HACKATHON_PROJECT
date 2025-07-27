import streamlit as st
import datetime

# Title
st.set_page_config(page_title="Emergency Alert", layout="centered")
st.title("🚨 Emergency Alert for Women's Safety")

# Emergency Contact Section
st.header("📞 Emergency Contact")
emergency_name = st.text_input("Contact Name", "My Guardian")
emergency_phone = st.text_input("Contact Phone Number", "+92XXXXXXXXXX")
if st.button("📤 Send Alert to Contact"):
    st.success(f"Alert sent to {emergency_name} at {emergency_phone}!")

# Siren Section
st.header("🔊 Play Siren")
try:
    with open("police_siren.mp3.mpeg", "rb") as siren_file:
        st.audio(siren_file.read(), format="audio/mp3")
except FileNotFoundError:
    st.warning("Siren file not found. Please upload 'police_siren.mp3.mpeg' in the Space.")

# Chat with AI
st.header("💬 Safety Check Chat")
user_input = st.text_input("How are you feeling?")
if user_input:
    response = "I'm here for you. You're not alone. If you're in danger, press the emergency button or contact someone you trust."
    st.write("🤖 AI Response:", response)

# Location Info (Placeholder - GPS not supported in Streamlit directly)
st.header("📍 Location (Mock)")
st.write("Unable to fetch live location. Please share manually.")
user_location = st.text_area("Enter your location (City, Street, etc.)")

# Emergency Time Log
st.write("⏱️ Time of Alert:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

st.markdown("---")
st.markdown("⚠️ This app is designed to assist in emergencies. Always call your local authorities if in immediate danger.")
