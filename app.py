import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
st.markdown("<h1 style='text-align: center;'>Vehicle sales analysis</h1>", unsafe_allow_html=True)
st.markdown("<h3 '>Data viewer</h3>", unsafe_allow_html=True)
filter_option = st.radio("Choose a filter:", ["None", "Automatic only", "Excellent condition", "4WD Only"])

if filter_option == "Automatic only":
    car_data = car_data[car_data["transmission"] == "automatic"]
elif filter_option == "Excellent condition":
    car_data = car_data[car_data["condition"] == "excellent"]
elif filter_option == "4WD Only":
    car_data = car_data[car_data["is_4wd"] == 1.0]

st.dataframe(car_data)

st.markdown("<h3 '>Scatter plot</h3>", unsafe_allow_html=True)
st.write('Creating a scatter plot for the car sales ads dataset')
fig = px.scatter(car_data, x="odometer", y="price")
st.plotly_chart(fig, use_container_width=True)


st.markdown("<h3 '>Create histogram</h3>", unsafe_allow_html=True)
hist_button = st.button('Create') # crear un botón
if hist_button:
    st.write('Creating a histogram for the car sales ads dataset')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


st.markdown("<h3 '>Compare models</h3>", unsafe_allow_html=True)
model1 = st.selectbox("Select first model:", car_data["model"].unique())
model2 = st.selectbox("Select second model:", car_data["model"].unique())
if st.button("Compare Models"):
    df_compare = car_data[car_data["model"].isin([model1, model2])]
    st.dataframe(df_compare)
    fig = px.histogram(
        df_compare, 
        x="price", 
        color="model", 
        title="Distribution of Prices per Model",
        labels={"price": "Precie (USD)", "model": "Model"},
        nbins=40, 
        barmode="overlay",
        opacity=0.6  
    )    
    st.plotly_chart(fig)


df = car_data.dropna(subset=["model_year", "condition"])
df["model_year"] = df["model_year"].astype(int)
st.markdown("<h3 '>Histogram of condition vs model year</h3>", unsafe_allow_html=True)
fig = px.histogram(
    df, 
    x="model_year", 
    color="condition", 
    labels={"model_year": "Model Year", "condition": "Condition"},
    nbins=len(df["model_year"].unique()),  
    barmode="stack"  
)

st.plotly_chart(fig)