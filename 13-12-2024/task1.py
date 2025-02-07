import streamlit as st
st.title("Hey!")
st.title("Even or Odd")
num1= st.number_input("Enter Number", min_value=1, step=1)
if st.button("Even/Odd"):
    if num1%2==0:
        st.success("Even number")
    else:
        st.error("Odd number")
name=st.text_input("Enter you name")
st.write(f"You entered {name}")
number = st.slider("Select a number", min_value=0, max_value=100, value=25)
st.write(f"You selected {number}")
if st.button("Click me"):
    st.write("Button Clicked!")
agree = st.checkbox("I agree to the terms")
if agree:
    st.write("You agreed!")
option = st.radio("Pick a color", ("Red", "Green", "Blue"))
st.write(f"You selected {option}")
choice = st.selectbox("Choose a fruit", ["Apple", "Banana", "Cherry"])
st.write(f"You selected {choice}")
uploaded_file = st.file_uploader("choose a file ")
if uploaded_file is not None:
    st.write(f"You uploaded: {uploaded_file.name}")
st.markdown("# This is a Markdown header")

