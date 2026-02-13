
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Training Satisfaction Dashboard", layout="wide")

st.title("Training Satisfaction Dashboard")

uploaded_file = st.file_uploader("Upload the training survey Excel file", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    
    st.subheader("Dataset Preview")
    st.dataframe(df.head())
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Overall Satisfaction Distribution")
        fig1, ax1 = plt.subplots()
        df["Ogólna satysfakcja (1–5)"].value_counts().sort_index().plot(kind="bar", ax=ax1)
        ax1.set_xlabel("Satisfaction Level (1–5)")
        ax1.set_ylabel("Number of Responses")
        st.pyplot(fig1)
    
    with col2:
        st.subheader("Average Ratings")
        avg_org = df["Ocena organizacji szkolenia (1–5)"].mean()
        avg_instr = df["Ocena prowadzącego (1–5)"].mean()
        fig2, ax2 = plt.subplots()
        ax2.bar(["Organization", "Instructor"], [avg_org, avg_instr])
        ax2.set_ylabel("Average Score (1–5)")
        st.pyplot(fig2)
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Training Met Expectations")
        fig3, ax3 = plt.subplots()
        df["Czy szkolenie spełniło oczekiwania (tak/nie)"].value_counts().plot(kind="bar", ax=ax3)
        ax3.set_xlabel("Response")
        ax3.set_ylabel("Number of Responses")
        st.pyplot(fig3)
    
    with col4:
        st.subheader("Most Valuable Element")
        fig4, ax4 = plt.subplots()
        df["Najbardziej wartościowy element"].value_counts().plot(kind="bar", ax=ax4)
        ax4.set_ylabel("Number of Responses")
        plt.xticks(rotation=45)
        st.pyplot(fig4)
    
    st.subheader("Average Satisfaction by Gender")
    fig5, ax5 = plt.subplots()
    df.groupby("Płeć")["Ogólna satysfakcja (1–5)"].mean().plot(kind="bar", ax=ax5)
    ax5.set_ylabel("Average Satisfaction (1–5)")
    st.pyplot(fig5)

else:
    st.info("Please upload an Excel file to generate the dashboard.")
