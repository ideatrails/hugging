from memory_profiler import profile
from transformers import pipeline


@profile
def run_model():
    sentiment_analysis = pipeline("sentiment-analysis")
    result = sentiment_analysis("I love programming with Hugging Face!")
    print(result)


if __name__ == "__main__":
    run_model()
