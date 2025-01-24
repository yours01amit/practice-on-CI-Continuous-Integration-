import streamlit as st

# Streamlit UI
st.title('Power Calculator')
st.write('Enter a number to calculate its square, cube, and fifth power')

# Get user input
num = st.number_input("Enter an int value", value=1, step=1)

# Calculate results
square = num**2
cube = num**3
fifth_power = num**5

# Display results

st.write(f'The square of {num} is: {square}')
st.write(f'The cube of {num} is: {cube}')
st.write(f'The fifth power of {num} is: {fifth_power}')