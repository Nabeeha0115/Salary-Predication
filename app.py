import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#Step 1: Load Data
st.title("Simple Linear Regression - Salary Prediction")
st.header("Step 1: Load and Display Data")
uploaded_file = st.file_uploader("Upload csv file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.dataframe(data)

    #Step 2: Visualize the Data
    st.header("Step 2: Visualize Salary vs Experience")
    fig, ax = plt.subplots()
    ax.scatter(data["YearsExperience"], data["Salary"], color='blue')
    ax.set_xlabel("Years of Experience")
    ax.set_ylabel("Salary")
    ax.set_title("Scatter plot")
    st.pyplot(fig)

    #Step 3: Train Model
    st.header("Step 3: Train Linear Regression Model")
    X = data[["YearsExperience"]]
    y = data["Salary"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    #X_train 80% data of i/p
    #X_test 20% data of i/p
    #y_train 80% data of o/p
    #y_test 20% data of o/p

    model = LinearRegression()
    model.fit(X_train, y_train)
    st.success("Model Trained Successfully!")


    #Step 4 : Visualize Regression Line
    st.header("Step 3: Visualize Regression Line") 
    fig2 , ax2 = plt.subplots()
    ax2.scatter(X.values.ravel(), y, color='blue', label='Actual Data')
    ax2.plot(X.values.ravel(), model.predict(X), color='red', label='Regression Line')
    ax2.set_xlabel("Years of Experience")
    ax2.set_ylabel("Salary")
    ax2.set_title("Regression Line on Data")
    ax2.legend()
    st.pyplot(fig2)

    # Step 5: Make Predictions    
st.header("Step 5: Predict Salary")

experience = st.number_input("Enter years of experience:")

if st.button("Predict Salary"):
    prediction = model.predict([[experience]])
    st.success(f"Predicted Salary: {prediction[0]:,.2f}")



    
