#Import libraries
import streamlit as st
import pandas as pd

#Application title
st.title("Data Dashboard")

# Upload the files
uploaded_file = st.file_uploader("Chose a CSV file", type = "csv")

if uploaded_file is not None:
    #Read the CSV file
    df = pd.read_csv(uploaded_file)

    #Display the data
    st.write("Data:")
    st.write(df)

    #Selectbox for columns
    columns = df.columns.tolist()
    columns_to_plot = st.selectbox("Select the columns to plot:", columns)

    #Plot the selected columns
    if columns_to_plot:
        st.write(f"Ploting column: {columns_to_plot}")
        st.line_chart(df[columns_to_plot])

else:
    st.write("Please upload a CSV file.")