# Text Summarizer using Transformers

This project implements an **abstractive text summarization model** using Hugging Face Transformers and the BART model.

---

## Features
- Uses pre-trained `facebook/bart-large-cnn`
- Generates concise summaries from long text
- Simple and easy-to-use pipeline
- Notebook-based implementation for experimentation

---

## 🛠️ Tech Stack
- Python
- PyTorch
- Hugging Face Transformers

---

## Installation

Run the following commands:

```bash
pip install torch==2.0.0+cu118 torchvision==0.15.1+cu118 torchaudio==2.0.0 --extra-index-url https://download.pytorch.org/whl/cu118
pip install transformers
````

---

## Usage

```python
from transformers import pipeline

def summarize_text(text, max_length=130, min_length=30):
    summarizer = pipeline(
        'summarization',
        model='facebook/bart-large-cnn',
        tokenizer='facebook/bart-large-cnn'
    )
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
```

---

## Example

**Input:**

```
The Eiffel Tower is a wrought-iron lattice tower...
```

**Output:**

```
The Eiffel Tower is a wrought-iron lattice tower in Paris, France...
```

---