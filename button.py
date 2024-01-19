import streamlit as st

# # Function to perform some calculations
# def perform_calculations(input_data):
#     # Perform calculations here
#     result = input_data * 2
#     return result

# # Main Streamlit app
# st.title("Multiple Outputs with Button")

# # Input widget (e.g., a slider)
# input_data = st.slider("Select a value", 0, 10, 5)

# # Button to trigger calculations
# if st.button("Calculate"):
#     # Perform calculations when the button is clicked
#     result = perform_calculations(input_data)
    
#     # Display the result
#     st.write(f"Result: {result}")

# # Additional output that persists even after button click
# st.text("This output remains visible regardless of the button click.")
# if st.button("Cal again"):
#     # Perform calculations when the button is clicked
#     result = perform_calculations(input_data)
    
#     # Display the result
#     st.write(f"Result: {result}")
import streamlit as st

# Function to perform multiplication
def multiply_numbers(a, b):
    return a * b

# Function to perform addition
def add_numbers(a, b):
    return a + b

# Main Streamlit app
st.title("Multiplication")

# Input widgets for numbers a and b
a = st.number_input("Enter value for a", value=2)
b = st.number_input("Enter value for b", value=3)

# Buttons to perform multiplication and addition
if st.button("Multiply"):
    multiplication_result = multiply_numbers(a, b)
    st.write(f"Multiplication Result: {multiplication_result}")
st.title("Addition Comparison")
if st.button("Add"):
    addition_result = add_numbers(a, b)
    st.write(f"Addition Result: {addition_result}")
