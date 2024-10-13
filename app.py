import streamlit as st

# Define functions for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Streamlit interface for the calculator
st.title("Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number", value=0.0, format="%f")
num2 = st.number_input("Enter second number", value=0.0, format="%f")

# Select operation
operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the calculation based on the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
        st.success(f"The result is: {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.success(f"The result is: {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.success(f"The result is: {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        st.success(f"The result is: {result}")
