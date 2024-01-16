import streamlit as st
import joblib



st.markdown("<h1 style='text-align:center'>Salary Prediction Model</h1>", unsafe_allow_html=True )
st.markdown("<h3 style='text-align:center'>Model to predict your Salary.</h3>", unsafe_allow_html=True )

Age= st.number_input("Enter your Age.",min_value=0)
Gender=st.radio('Select your Gender',['Male','Female'])
if Gender=='Male':
    Gender=1
else:
    Gender=0


Years_of_Experience =st.slider('Enter ypur Experience. (in years)',min_value=0, max_value= Age-20)

if st.button('Predict!'):
    model=joblib.load('Salary_model.h5')
    prediction=model.predict([[Age,Gender,Years_of_Experience]])
    st.success(round(prediction[0],2))