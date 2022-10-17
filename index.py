import sklearn
import pickle
import streamlit as st


st.header("⚕️ Prediction to Buy Insurance Based on age")

st.subheader('Using Logistic Regression')

age = st.slider('Enter your age ',10,100,50)

if st.button("Get Prediction"):
    pickle_m1 = pickle.load(open('m1.pkl','rb'))
    res = pickle_m1.predict([[age]])
    if res == 0:
        st.success("👨‍⚕️: ' No need to buy the insurance...! '")
    else :
        st.success("👨‍⚕️: ' You should buy insurance..! '")