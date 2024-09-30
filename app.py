import numpy as np
import streamlit as st
import pickle

# Load the pre-trained model
model = pickle.load(open('breast_cancer_detector.pkl', 'rb'))


# Function to make predictions
def predict(features):
    return model.predict(np.array(features).reshape(1, -1))[0]


# Streamlit app
st.title("Breast Cancer Detection")
st.write("### Enter the values of tumor features below:")

# Define the feature names
features = [
    "Mean Radius", "Mean Texture", "Mean Perimeter", "Mean Area",
    "Mean Smoothness", "Mean Compactness", "Mean Concavity",
    "Mean Concave Points", "Mean Symmetry", "Mean Fractal Dimension",
    "Radius Error", "Texture Error", "Perimeter Error", "Area Error",
    "Smoothness Error", "Compactness Error", "Concavity Error",
    "Concave Points Error", "Symmetry Error", "Fractal Dimension Error",
    "Worst Radius", "Worst Texture", "Worst Perimeter", "Worst Area",
    "Worst Smoothness", "Worst Compactness", "Worst Concavity",
    "Worst Concave Points", "Worst Symmetry", "Worst Fractal Dimension"
]

# Create input fields in a grid format
values = []
col_count = 3  # Number of columns in the layout
for i in range(0, len(features), col_count):
    cols = st.columns(col_count)  # Create a row of columns
    for j, col in enumerate(cols):
        if i + j < len(features):
            value = col.number_input(features[i + j], value=0.0)
            values.append(value)

# Prediction button
if st.button("Predict Cancer"):
    output = predict(values)

    if output == 0:
        st.markdown(
            "**Result:** Patient has **Breast Cancer**.")
    else:
        st.markdown(
            "**Result:** Patient has **No Breast Cancer**.")

# Run the app with: streamlit run app.py
