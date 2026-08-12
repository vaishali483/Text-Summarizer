from transformers import pipeline

def summarize_text(text, max_length=130, min_length=30):
    """
    Summarizes the input text using a pre-trained summarization model.

    Parameters:
    - text (str): The text to summarize.
    - max_length (int): Maximum length of the summary.
    - min_length (int): Minimum length of the summary.

    Returns:
    - summary_text (str): The summarized text.
    """
    # Load pre-trained summarization model
    summarizer = pipeline('summarization', model='facebook/bart-large-cnn', tokenizer='facebook/bart-large-cnn')

    # Summarize the input text
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)

    return summary[0]['summary_text']

if __name__ == "__main__":
    # Example text for summarization
    text = """
    The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It was named after the engineer Gustave Eiffel, whose company designed and built the structure. The tower was completed in 1889 and was initially criticized by some of France's leading artists and intellectuals for its design, but it has become a global cultural icon of France and one of the most recognizable structures in the world. The Eiffel Tower is the most-visited paid monument in the world, with millions of people ascending it every year.
    """

    # Get the summary
    summary = summarize_text(text)
    print("Original Text:")
    print(text)
    print("\nSummary:")
    print(summary)
