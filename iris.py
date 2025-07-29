import pickle
import streamlit as st
model1=pickle.load(open("iris.pkl","rb"))

def mydeploy():
     st.title("Iris Flower Prediction")
     sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, step=0.1)
     sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, step=0.1)
     petal_length = st.number_input("Petal Length (cm)", min_value=0.0, step=0.1)
     petal_width = st.number_input("Petal Width (cm)", min_value=0.0, step=0.1)
     if st.button("Predict"):
        features = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = model1.predict(features)[0]
        label_map = {
            0: "Setosa",
            1: "Versicolor",
            2: "Virginica"
        }
        st.success(f"The predicted Iris species is: **{label_map.get(prediction, 'Unknown')}**")

mydeploy()
    
