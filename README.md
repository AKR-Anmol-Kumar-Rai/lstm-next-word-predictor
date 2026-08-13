# 🧠 LSTM Next Word Predictor

<p align="center">

  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/PyTorch-LSTM-ee4c2c?style=for-the-badge&logo=pytorch" />
  <img src="https://img.shields.io/badge/NLP-Natural%20Language%20Processing-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker" />

</p>

<p align="center">
  <b>An end-to-end NLP application for predicting the next word using a trained LSTM neural network.</b>
</p>

<p align="center">
  <b>Created by Anmol Kumar Rai</b>
</p>

---

## 🚀 Live Demo

<p align="center">

<a href="https://lstm-next-word-predictor01.streamlit.app/">
  <img src="https://img.shields.io/badge/🚀%20LIVE%20DEMO-Streamlit-red?style=for-the-badge" />
</a>

</p>

🌐 **Application:**
https://lstm-next-word-predictor01.streamlit.app/

---

# 📌 Project Overview

**LSTM Next Word Predictor** is a word-level Natural Language Processing project that uses a **Long Short-Term Memory (LSTM)** neural network to predict the next word in a sequence.

The project takes a sentence entered by the user, processes the text, converts the words into numerical token IDs, pads the sequence to the required length, and passes it through a trained LSTM model.

The model then produces scores for the words in its vocabulary and selects the word with the highest score as the predicted next word.

The complete project covers:

* NLP preprocessing
* Vocabulary creation
* Word-to-index conversion
* Sequence padding
* Word embeddings
* LSTM sequence modeling
* Model training
* Model saving and loading
* Model inference
* Streamlit application development
* Docker containerization
* Cloud deployment

---

# 🎯 What Does the Application Do?

The application performs **next-word prediction using a trained LSTM neural network**.

It provides an interactive Streamlit interface where the user can enter a sentence or a sequence of words. The application then processes the entered text and uses the trained LSTM model to predict the word that is most likely to appear next.

For example, if the user enters:

```text
I am learning
```

the application analyzes the sequence of words and predicts a possible next word based on the patterns learned from the training dataset.

If the model predicts **Python**, the application displays:

```text
I am learning Python
```

---

# 🔄 What Happens After the User Enters Text?

The prediction does not happen directly from the raw sentence. The application performs several preprocessing and inference steps before generating the final prediction.

```text
User enters sentence
        ↓
Convert text to lowercase
        ↓
Tokenize the sentence using NLTK
        ↓
Convert words into token IDs
        ↓
Handle unknown words using <unk>
        ↓
Pad the sequence to the required length
        ↓
Convert the sequence into a PyTorch tensor
        ↓
Pass the tensor through the trained LSTM model
        ↓
Generate scores for all words in the vocabulary
        ↓
Select the word with the highest score
        ↓
Convert the predicted token ID back into a word
        ↓
Display the predicted next word
```

---

# 🧠 How Does the Model Decide the Next Word?

The trained LSTM has learned relationships between words from the training dataset.

During training, the dataset is converted into input-target pairs. Each input sequence contains one or more words, while the corresponding target is the word that should come next.

For example:

| Input Sequence     | Target Word |
| ------------------ | ----------- |
| `I am`             | `learning`  |
| `I am learning`    | `Python`    |
| `machine learning` | `is`        |

By processing many such sequences during training, the LSTM learns patterns and relationships between words. These learned patterns allow the model to estimate which word is most likely to appear after a given sequence.

During prediction, the model produces a score for every word in its vocabulary.

For example:

| Word       | Model Score |
| ---------- | ----------: |
| `python`   |        5.82 |
| `machine`  |        3.41 |
| `learning` |        2.76 |
| `model`    |        1.94 |
| `data`     |        4.12 |

The application selects the word with the **highest score**.

In this example:

```text
python → 5.82
```

Therefore, **Python** becomes the predicted next word.

The final output would be:

```text
Input:
I am learning

Prediction:
Python

Final sentence:
I am learning Python
```
