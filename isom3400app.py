# Write your code below
import streamlit as st
import pandas as pd

st.title("Simple Contact Form")
st.write("Enter your details below. Data saves automatically to a CSV file.")

# --- File path ---
CSV_FILE = "contacts.csv"

# --- THE FORM ---
with st.form(key = "my_form"):
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    fav_number = st.number_input("Favourite Number", min_value = 0, step = 1)
    
    submitted = st.form_submit_button("Submit Contact")

# --- LOGIC AFTER THE FORM ---
if submitted:
    # Validation
    if not first_name or not last_name:
        st.error("First Name and Last Name are required!")
    else:
        # Prepare the new row
        new_data = pd.DataFrame({
            "First Name": [first_name],
            "Last Name": [last_name],
            "Favourite Number": [fav_number]
        })
        
        # Save to CSV (try reading existing data, if fails start fresh)
        try:
            existing_data = pd.read_csv(CSV_FILE)
            updated_data = pd.concat([existing_data, new_data], ignore_index = True)
        except FileNotFoundError:
            # File doesn't exist yet, this is the first entry
            updated_data = new_data
        
        # Write the updated data back to CSV
        updated_data.to_csv(CSV_FILE, index = False)
        
        st.success(f"Saved {first_name} {last_name} to the database!")
        st.balloons()

# --- DISPLAY EXISTING DATA ---
st.subheader("Current Contact List")

try:
    df = pd.read_csv(CSV_FILE)
    st.dataframe(df, use_container_width = True)
except FileNotFoundError:
    st.info("No contacts saved yet. Use the form above to add one.")
