# -*- coding: utf-8 -*-
import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for Prediction

def fetal_prediction(input_data):


    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 2):
      return 'The fetus is suspected to be pathological'
    else:
      return 'The fetus is normal'



def main():


    # giving a title
    st.title('Fetal Health Prediction Web App')


    # getting the input data from the user


    hr = st.text_input('Baseline Heart Rate')
    acc = st.text_input('Accelerations per Second')
    mov = st.text_input('Fetal Movements per Second')
    ute = st.text_input('Uterine Contractions per Second')
    ld = st.text_input('Light Decelerations per Second')
    sd = st.text_input('Severe Decelerations per Second')
    pd = st.text_input('Prolonged Decelerations per Second')
    abs = st.text_input('Abnormal Short Term Variabilities')
  


    # code for Prediction
    diagnosis = ''

    # creating a button for Prediction

    if st.button('Fetal Health Test Result'):
        diagnosis = fetal_prediction([hr,acc,mov,ute,ld,sd,pd,abs])


    st.success(diagnosis)





if __name__ == '__main__':
    main()

