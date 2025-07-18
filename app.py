import torch
import streamlit as st
from transformers import pipeline

st.title("Text Summarizer")

text = st.text_area("Enter a paragraph,text...")
model_selection = st.selectbox("Select a model",["facebook/bart-large-cnn", "google/pegasus-xsum"])

if st.button("Summarizer"):
    if text:
        summarizer = pipeline("summarization", model=model_selection)
        summary = summarizer(text, max_length=200, min_length=120, do_sample=False)
        st.write("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.error("Please enter some text to summarize.")
