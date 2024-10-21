import streamlit as st
from datetime import datetime, timedelta

# Function to calculate age in various time units
def calculate_age(dob):
    now = datetime.now()
    dob_datetime = datetime.combine(dob, datetime.min.time())
    delta = now - dob_datetime

    years = delta.days // 365
    delta -= timedelta(days=years * 365)
    months = delta.days // 30
    delta -= timedelta(days=months * 30)
    weeks = delta.days // 7
    delta -= timedelta(days=weeks * 7)
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return years, months, weeks, days, hours, minutes, seconds

# Function to list which weekday the birthday fell on each year
def birthday_weekdays_by_year(dob):
    now = datetime.now()
    birthday_days = []

    for year in range(dob.year, now.year + 1):
        this_year_birthday = datetime(year, dob.month, dob.day)
        weekday_name = this_year_birthday.strftime('%A')  # Get weekday name
        birthday_days.append((year, weekday_name))

    return birthday_days

# Streamlit application
st.set_page_config(page_title="Age Calculator", layout="wide")
st.title("🎉 Age Calculator 🎉")
st.markdown("## Find out how old you are in various time units!")

# Current date for setting the range
today = datetime.today()

# Date input with extended range
dob_input = st.date_input(
    "Enter your Date of Birth:",
    value=today,  # Default value as today
    min_value=datetime(1900, 1, 1),  # Minimum date (adjust as needed)
    max_value=today  # Maximum date is today
)

# Layout with columns
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Your Age Breakdown:")
    if st.button("Calculate Age"):
        if dob_input:
            years, months, weeks, days, hours, minutes, seconds = calculate_age(dob_input)
            st.success(f"🎂 You are **{years} years, {months} months, {weeks} weeks, {days} days, "
                       f"{hours} hours, {minutes} minutes, and {seconds} seconds** old!")

            birthday_days = birthday_weekdays_by_year(dob_input)
            st.subheader("Weekday of Your Birthday Each Year:")

            # Displaying birthdays side-by-side, 5 years per row
            for i in range(0, len(birthday_days), 5):
                cols = st.columns(5)  # Create 5 columns
                for j, (year, weekday) in enumerate(birthday_days[i:i+5]):
                    cols[j].write(f"**{year}:** {weekday}")

            st.balloons()  # Celebrate with balloons
        else:
            st.error("Please enter your date of birth to calculate your age.")

with col2:
    st.image("https://source.unsplash.com/400x400/?birthday", caption="Celebrate your Age!", use_column_width=True)

# Additional message and visualization
st.markdown("---")
st.markdown("### 🥳 Celebrate your life! Remember, age is just a number. Keep shining bright!")
st.markdown("Here's a quick reminder to enjoy every moment of your life!")

# Example visualization
st.subheader("Fun Age Facts:")
age_facts = [
    "You share your birthday with approximately 20,000 people worldwide!",
    "Your age is just a number, but the experiences you gather are priceless!",
    "Every year brings new opportunities and adventures. Embrace them!"
]
for fact in age_facts:
    st.markdown(f"- {fact}")

# Inspirational Quote
st.markdown("---")
st.markdown("### ✨ Inspirational Quote:")
st.markdown("**'Count your age by friends, not years. Count your life by smiles, not tears.' - John Lennon**")

# Footer
st.markdown("---")
