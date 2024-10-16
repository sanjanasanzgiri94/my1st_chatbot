import openai
import streamlit as st

# Access the API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to generate text with continuous stream
def analyze_sentiment(review, category):
    prompt = f"Analyze the sentiment of the following {category} review and classify it as Positive, Negative, or Neutral:\n\nReview: {review}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a sentiment analysis assistant."},
            {"role": "user", "content": prompt},
        ]
    )

    # Extract the sentiment analysis from GPT's response
    sentiment = response['choices'][0]['message']['content']
    return sentiment.strip()

# Function to get user input in Colab and display the result
def main():
    # Get input from user using Colab input fields
    category = input("Enter the category of the review (e.g., Food, Product, Place, Other): ").capitalize()
    review = input(f"Enter your {category.lower()} review: ")

    # Analyze the sentiment of the review
    if review:
        sentiment = analyze_sentiment(review, category)
        print(f"\nSentiment Analysis Result: {sentiment}")
    else:
        print("Please enter a valid review.")

# Run the main function
main()
   
