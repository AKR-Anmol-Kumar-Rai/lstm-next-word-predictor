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

- NLP preprocessing
- Vocabulary creation
- Word-to-index conversion
- Sequence padding
- Word embeddings
- LSTM sequence modeling
- Model training
- Model saving and loading
- Model inference
- Streamlit application development
- Docker containerization
- Cloud deployment

---

# 🎯 What Does the Application Do?

The application performs **next-word prediction**.

The user enters a sentence into the Streamlit interface.

