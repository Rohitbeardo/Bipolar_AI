import streamlit as st
import pickle
import numpy as np
from sklearn import *

pickle_in = open('input.pkl', 'rb') 
classifier = pickle.load(pickle_in)

def prediction(mood,motivation,attention,irritability,anxiety,sleep_quality,caffeine,active_time):   
    arr = np.array([mood,motivation,attention,irritability,anxiety,sleep_quality,caffeine,active_time]).reshape(1,-1)
    prediction = classifier.predict_proba(arr)
    category = np.argmax(prediction) +1
    if category == 0:
        return "The patient could be tending towards a Mania episode"
    elif category == 1:
        return "The patient could be tending towards a Depression episode"
    else:
        return "The patient is in a normal state"

def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Bipolar Disorder Diagnosis</h1> 
    </div> """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    mood = st.number_input("Enter mood value between (-3,2)")
    motivation = st.number_input("Enter motivation value between (-3,3)")
    attention = st.number_input("Enter attention value between (1,4)")
    irritability = st.number_input("Enter irritability value between (1,5)")
    anxiety = st.number_input("Enter anxiety value between (1,4)")
    sleep_quality = st.number_input("Enter sleep_quality value between (1,5)")
    caffeine = st.number_input("Enter caffeine value between (0,900)")
    active_time = st.number_input("Enter active_time value between (0,2000)")

    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    col1, col2, col3 , col4, col5 = st.beta_columns(5)
    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3 :
         center_button = st.button('Predict')
         result = prediction(mood,motivation,attention,irritability,anxiety,sleep_quality,caffeine,active_time)
    st.success(result)


if __name__ == '__main__':
    main()
