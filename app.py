import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import time

# Function to calculate age and occurrences
def calculate_age_and_occurrences(dob):
    now = datetime.now()
    dob_datetime = datetime.combine(dob, datetime.min.time())

    # Calculate years, months, weeks, and days
    years = now.year - dob_datetime.year
    months = now.month - dob_datetime.month
    weeks = (now - dob_datetime).days // 7
    days = (now - dob_datetime).days % 7

    # Initialize dictionary to count birthdays by day of the week and store years
    birthday_counts = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

    # Count occurrences of birthdays by day of the week and store the corresponding years
    for year in range(dob_datetime.year, now.year + 1):
        try:
            # Handle leap year edge case with try-except
            birthday = datetime(year, dob_datetime.month, dob_datetime.day)
            day_name = birthday.strftime("%A")
            birthday_counts[day_name].append(year)
        except ValueError:
            # Skip if the date is invalid (like Feb 29 on non-leap years)
            pass

    # Calculate total hours, minutes, and seconds since birth
    total_seconds_since_birth = (now - dob_datetime).total_seconds()
    hours = int(total_seconds_since_birth // 3600)
    minutes = int((total_seconds_since_birth % 3600) // 60)
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
        years, months, weeks, days, hours, minutes, seconds, birthday_counts = calculate_age_and_occurrences(dob_input)

        # Display age with hours, minutes, and seconds
        age_message = (
            f"🎂 You are **{years} years, {months} months, {weeks} weeks, "
            f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds** old!"
        )
        st.success(age_message)
        st.balloons()

        # Display occurrences of your birthday
        st.caption("Occurrences of Your Birthday by Day of the Week")
        occurrence_message = "🗓️ Your birthday has occurred on "
        for day, count in birthday_counts.items():
            occurrence_message += f"{len(count)} {day}s, "
        occurrence_message = occurrence_message[:-2] + " since your birth!"

        st.write(occurrence_message)

        # Prepare data for the bar chart
        occurrences_df = pd.DataFrame([(day, len(years)) for day, years in birthday_counts.items()], columns=['Day', 'Count'])
        days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        occurrences_df['Day'] = pd.Categorical(occurrences_df['Day'], categories=days_order, ordered=True)
        occurrences_df = occurrences_df.sort_values('Day')

        # Display bar chart
        st.bar_chart(occurrences_df.set_index('Day')['Count'])
        

        # Display years in which the birthday fell on each day in a table format
        st.markdown("### 📅 Years in Which Your Birthday Fell on Each Day:")
        for day in days_order:
            st.write(f"**{day}:**", ", ".join(map(str, birthday_counts[day])))

        st.markdown("### ── .✦ Live your life with no excuses, travel with no regret, and age with no fear! ── .✦")
        # Live tracking of current time and elapsed time
        live_counter = st.empty()
        while True:
            now = datetime.now()
            total_seconds_since_birth = (now - datetime.combine(dob_input, datetime.min.time())).total_seconds()
            hours = int(total_seconds_since_birth // 3600)
            minutes = int((total_seconds_since_birth % 3600) // 60)
            seconds = int(total_seconds_since_birth % 60)
            current_time = now.strftime("%H:%M:%S")

            
            time.sleep(1)

    else:
        st.error("Please select your date of birth to calculate your age.")

st.markdown("---")
st.markdown("### 🥳 Celebrate your life! Remember, age is just a number. Keep shining bright!")
