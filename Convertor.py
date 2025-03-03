#Project 01: Unit Convertor
#Build a Google Unit Convertor using Python and streamlit

import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3)
        padding:30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1{
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton>button{
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: white;
        font-size: 18px;
        paddingL: 10px 20px;
        transition: 0.3s;
        border-radius: 10px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover{
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        transform: scale(1.05);
         color: black;
    }
    .result-box {
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        background: linear-gradient(45deg, #0b5394, #351c75);
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
        margin-top: 20px;
    }
    .footer{
        text-align: center;
        font-size: 14px;
        color: black;
        marging-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#title and description:
st.markdown("<h1> Unit Convertor using Python and Streamlit </h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length , weight, and temperature.")

#sidebar menu:
conversion_type = st.sidebar.selectbox("Choose Conversion Type", [ "Length", "Weight", "Temprature"])
value =st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilograms", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feets"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilograms", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feets"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces", "Miligrams"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces", "Miligrams"])
elif conversion_type == "Temprature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

#converted function:
def length_convertor(value, from_unit, to_unit):
    length_units ={
        "Meters": 1, "Kilometers": 0.001, "Centermeters": 100, "Millimeters": 1000,
         "Miles": 0.000621371, "Yards": 1.09361, "Inches": 39.37, "Feets": 3.28
    }
    return (value / length_units[from_unit] *  length_units[to_unit])

def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        "Kilogram": 1, "Grams": 1000, "Pounds": 2.2046, "Ounces": 35.27, "Miligrams": 1000000
    }
    return (value / weight_units[from_unit] /  weight_units[to_unit])

def temprature_convertor(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 +32) if to_unit == "Fahrenheit" else (value + 273.15 if to_unit == "Kelvin" else value)
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

#button for conversion:
if st.button("🤖Convert"):
    if conversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temprature":
        result = temprature_convertor(value, from_unit, to_unit)

    #Result ko dikhana (Conversion ka result show karna)
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

#footer (Neeche footer message)
st.markdown("<div class='footer'>Created with ❤️ by Areej Shah </div>", unsafe_allow_html=True)



     


 