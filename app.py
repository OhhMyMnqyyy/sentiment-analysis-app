import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sentiment_model import analyze_sentiment

# Streamlit UI
st.title("Customer Review Sentiment Analysis")

# User input
review = st.text_area("Enter a customer review:")

if st.button("Analyze Sentiment"):
    sentiment = analyze_sentiment(review)
    st.write(f"### Sentiment: {sentiment}")

# Example dataset
st.subheader("Sample Review Data")
sample_data = pd.DataFrame({
    "Review": ["I love this product!", "It was okay.", "Worst experience ever!"],
    "Sentiment": ["Positive 😊", "Neutral 😐", "Negative 😡"]
})
st.write(sample_data)

# Visualizing Sentiment Distribution
st.subheader("Sentiment Distribution (Example)")
fig, ax = plt.subplots()
sample_data["Sentiment"].value_counts().plot(kind="bar", ax=ax, color=["green", "blue", "red"])
st.pyplot(fig)

