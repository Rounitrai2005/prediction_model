import streamlit as st
import pandas as pd
import joblib

# Load model and feature names
model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

st.set_page_config(page_title="Housing Price Predictor", layout="centered")

st.title("🏠 Housing Price Prediction")
st.write("Enter the details below to estimate the house price.")

longitude = st.number_input("Longitude", value=-122.23)
latitude = st.number_input("Latitude", value=37.88)
housing_median_age = st.number_input("House Age", value=20)
total_rooms = st.number_input("Total Rooms", value=2000)
total_bedrooms = st.number_input("Total Bedrooms", value=400)
population = st.number_input("Population", value=1000)
households = st.number_input("Households", value=350)
median_income = st.number_input("Median Income", value=5.0)

ocean = st.selectbox(
    "Ocean Proximity",
    [
        "INLAND",
        "NEAR BAY",
        "NEAR OCEAN",
        "ISLAND",
        "<1H OCEAN"
    ]
)

# Create input dataframe
input_df = pd.DataFrame([[0] * len(columns)], columns=columns)

input_df["longitude"] = longitude
input_df["latitude"] = latitude
input_df["housing_median_age"] = housing_median_age
input_df["total_rooms"] = total_rooms
input_df["total_bedrooms"] = total_bedrooms
input_df["population"] = population
input_df["households"] = households
input_df["median_income"] = median_income

dummy = "ocean_proximity_" + ocean

if dummy in input_df.columns:
    input_df[dummy] = 1

if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]

    st.success(f"Predicted House Price: ${prediction:,.2f}")