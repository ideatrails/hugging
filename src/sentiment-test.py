from transformers import pipeline

sentiment_analysis = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)
input_text = "I love you so much, but we have to part forever."
result = sentiment_analysis(input_text)
print(result)
