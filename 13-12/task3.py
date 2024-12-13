import streamlit as st
project_score=st.number_input("Enter your Project score")
internal_score=st.number_input("Enter your Internal score")
external_score=st.number_input("Enter your External score")
total_score=0
if(project_score and internal_score and external_score > 50):
    total_score=((project_score * 70)/100 + (internal_score*10)/100) + ((external_score *20)/100)
    st.title(f"Total score is {total_score}")
else:
    if (project_score<=50):
        st.title(f"Failed in project,score is: { project_score}")
    if (internal_score <= 50):
        st.title(f"Failed in internal,score is: {internal_score}")
    if (external_score<= 50):
       st.title(f"Failed in external,score is: {external_score}")

if(total_score>90):
    st.title("A grade")
elif(total_score>80):
    st.title("B grade")
elif(total_score>50):
    st.title("c grade")
