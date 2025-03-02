import streamlit as st
import nltk
import string
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text):
    # Lowercase the text
    text = text.lower()
    
    # Remove emails
    email_pattern = r'[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+'
    emails = re.findall(email_pattern, text)
    text = re.sub(email_pattern, '', text)
    
    # Remove phone numbers
    phone_pattern = r'\b\d{10}\b|\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4}'
    phones = re.findall(phone_pattern, text)
    text = re.sub(phone_pattern, '', text)
    
    # Remove special characters (excluding spaces and alphanumeric characters)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # Summary report
    report = {
        "Total Tokens": len(tokens),
        "Tokens after Cleaning": len(filtered_tokens),
        "Removed Emails": emails,
        "Removed Phone Numbers": phones,
    }
    
    return ' '.join(filtered_tokens), report

# Streamlit UI
st.title("Text Cleaner Tool")
st.write("Enter your raw text below, and the cleaned version will be displayed with a summary report.")

# User input
user_input = st.text_area("Enter text here:", "")

if st.button("Clean Text"):
    if user_input:
        cleaned_text, report = clean_text(user_input)
        st.subheader("Cleaned Text:")
        st.write(cleaned_text)
        
        st.subheader("Summary Report:")
        st.write(report)
    else:
        st.warning("Please enter some text to clean.")