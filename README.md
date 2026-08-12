# Text Summarizer using Transformers

This project implements an **abstractive text summarization model** using Hugging Face Transformers and the BART model.

---

## Features
- Uses pre-trained `facebook/bart-large-cnn`
- Generates concise summaries from long text
- Simple and easy-to-use pipeline
- Notebook-based implementation for experimentation

---

## Tech Stack
- Python
- PyTorch
- Hugging Face Transformers

---

## Installation

Run the following commands:

```bash
pip install torch==2.0.0+cu118 torchvision==0.15.1+cu118 torchaudio==2.0.0 --extra-index-url https://download.pytorch.org/whl/cu118
pip install transformers
pip install huggingface-hub==0.30.0
````

---

## Usage

Run `` summarise.py ``

---

## Example

**Input:**

The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It was named after the engineer Gustave Eiffel, whose company designed and built the structure. The tower was completed in 1889 and was initially criticized by some of France's leading artists and intellectuals for its design, but it has become a global cultural icon of France and one of the most recognizable structures in the world. The Eiffel Tower is the most-visited paid monument in the world, with millions of people ascending it every year.


**Output:**


The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. The tower was completed in 1889 and was initially criticized by some of France's leading artists and intellectuals for its design.


---