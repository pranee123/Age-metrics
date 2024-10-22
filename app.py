import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import time  # Import the time module

# Function to calculate age and occurrences
def calculate_age_and_occurrences(dob):
    now = datetime.now()
    dob_datetime = datetime.combine(dob, datetime.min.time())  # Convert to datetime

    # Calculate years, months, weeks, and days
    years = now.year - dob_datetime.year
    months = now.month - dob_datetime.month
    weeks = (now - dob_datetime).days // 7
    days = (now - dob_datetime).days % 7

    # Initialize a dictionary to count occurrences by day of the week
    birthday_counts = {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0
    }

    # Count occurrences of birthdays by day of the week
    for year in range(dob_datetime.year, now.year + 1):
        birthday = datetime(year, dob_datetime.month, dob_datetime.day)
        day_name = birthday.strftime("%A")  # Get the day name
        birthday_counts[day_name] += 1

    # Calculate total hours, minutes, and seconds since birth
    total_seconds_since_birth = (now - dob_datetime).total_seconds()
    hours = int(total_seconds_since_birth // 3600)
    minutes = int((total_seconds_since_birth % 3600) // 60)  # Calculate minutes
    seconds = int(total_seconds_since_birth % 60)

    return years, months, weeks, days, hours, minutes, seconds, birthday_counts

# Streamlit application
st.set_page_config(page_title="Age Calculator", layout="wide")
st.title("🎉 Age Calculator 🎉")

# User input for DOB using a calendar date input
dob_input = st.date_input("Select your Date of Birth:", value=datetime.today(), min_value=datetime(1900, 1, 1))

# Layout for the age calculation
if st.button("Calculate Age"):
    if dob_input:
        # Calculate age and occurrences
        years, months, weeks, days, hours, minutes, seconds, birthday_counts = calculate_age_and_occurrences(dob_input)

        # Display age along with hours, minutes, and seconds beside it
        age_message = (
            f"🎂 You are **{years} years, {months} months, {weeks} weeks, "
            f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds** old!"
        )
        st.success(age_message)

        # Trigger balloons effect
        st.balloons()

        # Prepare the birthday occurrence message
        st.caption("Occurrences of Your Birthday by Day of the Week")
        occurrence_message = "🗓️ Your birthday has occurred on "
        for day, count in birthday_counts.items():
            occurrence_message += f"{count} {day}s, "
        
        # Remove the trailing comma and space
        occurrence_message = occurrence_message[:-2] + " since your birth!"
        
        # Display the birthday occurrence message
        st.write(occurrence_message)
        
        # Prepare data for bar chart and change order of days
        occurrences_df = pd.DataFrame(list(birthday_counts.items()), columns=['Day', 'Count'])
        
        # Specify the desired order of the days
        days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        # Reorder the DataFrame based on the custom day order
        occurrences_df['Day'] = pd.Categorical(occurrences_df['Day'], categories=days_order, ordered=True)
        occurrences_df = occurrences_df.sort_values('Day')
        
        # Displaying the bar chart using Streamlit's st.bar_chart
        st.bar_chart(occurrences_df.set_index('Day')['Count'])
        # st.markdown("### 👑 Live your life with no excuses, travel with no regret, and age with no fear!๋࣭ ⭑⚝")
        st.markdown("### ── .✦ Live your life with no excuses, travel with no regret, and age with no fear! ── .✦")
        # Live tracking for current time and elapsed time
        live_counter = st.empty()  # Create a placeholder for live tracking

        while True:
            now = datetime.now()
            # Calculate the total hours, minutes, and seconds since the birth date
            total_seconds_since_birth = (now - datetime.combine(dob_input, datetime.min.time())).total_seconds()
            hours = int(total_seconds_since_birth // 3600)
            minutes = int((total_seconds_since_birth % 3600) // 60)  # Calculate minutes
            seconds = int(total_seconds_since_birth % 60)
            current_time = now.strftime("%H:%M:%S")  # Get current time in HH:MM:SS format
            
            # Update the placeholder with current time and elapsed time
            
            
            # Sleep for 1 second to update every second
            time.sleep(1)

    else:
        st.error("Please select your date of birth to calculate your age.")
    
# Additional message

st.markdown("### 🥳 Celebrate your life! Remember, age is just a number. Keep shining bright!")
st.markdown("---")

