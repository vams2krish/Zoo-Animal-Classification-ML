import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

#load the pickle files
predicted_animal = pickle.load(open('model.pkl','rb'))


def user_input_features(predicted_price):
    st.title('Zoo Animal Type Prediction')
    st.header('User Input Features')
    hair = st.slider('Hair (0 = No, 1 = Yes)', 0, 1, 0)
    feathers = st.slider('Feathers (0 = No, 1 = Yes)', 0, 1, 0)
    eggs = st.slider('Eggs (0 = No, 1 = Yes)', 0, 1, 0)
    milk = st.slider('Milk (0 = No, 1 = Yes)', 0, 1, 0)
    airborne = st.slider('Airborne (0 = No, 1 = Yes)', 0, 1, 0)
    aquatic = st.slider('Aquatic (0 = No, 1 = Yes)', 0, 1, 0)
    predator = st.slider('Predator (0 = No, 1 = Yes)', 0, 1, 0)
    toothed = st.slider('Toothed (0 = No, 1 = Yes)', 0, 1, 0)
    backbone = st.slider('Backbone (0 = No, 1 = Yes)', 0, 1, 0)
    breathes = st.slider('Breathes (0 = No, 1 = Yes)', 0, 1, 0)
    venomous = st.slider('Venomous (0 = No, 1 = Yes)', 0, 1, 0)
    fins = st.slider('Fins (0 = No, 1 = Yes)', 0, 1, 0)
    legs = st.slider('Legs (Number)', 0, 8, 0)
    tail = st.slider('Tail (0 = No, 1 = Yes)', 0, 1, 0)
    domestic = st.slider('Domestic (0 = No, 1 = Yes)', 0, 1, 0)
    catsize = st.slider('Catsize (0 = No, 1 = Yes)', 0, 1, 0)

    # Store user input into a dictionary
    user_input = {
            'hair': hair, 'feathers': feathers, 'eggs': eggs, 'milk': milk,
            'airborne': airborne, 'aquatic': aquatic, 'predator': predator,
            'toothed': toothed, 'backbone': backbone, 'breathes': breathes,
            'venomous': venomous, 'fins': fins, 'legs': legs, 'tail': tail,
            'domestic': domestic, 'catsize': catsize
        }
    features = pd.DataFrame(user_input, index=[0])
    return features




input_df = user_input_features(predicted_animal)

# Predict using the Linear Regression model
prediction = predicted_animal.predict(input_df)



#Click Button 
if st.button("submit"):
    st.write(f"The predicted animal is {prediction[0]}")


    





